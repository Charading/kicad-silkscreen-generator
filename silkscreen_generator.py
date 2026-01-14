"""
KiCad Silkscreen Label Generator Plugin
Duplicates and increments silkscreen labels with custom offsets
"""

import pcbnew
import wx
import re
import os
from .dialog import SilkscreenGeneratorDialog


class SilkscreenGeneratorPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Silkscreen Label Generator"
        self.category = "Modify PCB"
        self.description = "Duplicate and increment silkscreen labels with custom offsets"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
    
    def Run(self):
        # Get the current board
        board = pcbnew.GetBoard()
        
        # Get selected items
        selected_items = [item for item in board.GetDrawings() 
                         if item.IsSelected() and item.Type() == pcbnew.PCB_TEXT_T]
        
        if not selected_items:
            wx.MessageBox(
                "Please select at least one silkscreen text label first!",
                "No Selection",
                wx.OK | wx.ICON_WARNING
            )
            return
        
        # Show dialog with the first selected item as reference
        source_text = selected_items[0]
        dialog = SilkscreenGeneratorDialog(None, source_text, len(selected_items))
        
        if dialog.ShowModal() == wx.ID_OK:
            # Get parameters from dialog
            params = dialog.GetValues()
            
            # Generate labels for each selected item
            for source_text in selected_items:
                self.generate_labels(board, source_text, params)
            
            # Refresh the board
            pcbnew.Refresh()
        
        dialog.Destroy()
    
    def generate_labels(self, board, source_text, params):
        """Generate duplicated labels with incremented numbers"""
        count = params['count']
        increment = params['increment']
        offset_x = params['offset_x']
        offset_y = params['offset_y']
        
        # Get the source text value
        source_value = source_text.GetText()
        
        # Extract number from text (if any)
        number_match = re.search(r'(\d+)', source_value)
        
        if number_match:
            # Text contains a number
            base_number = int(number_match.group(1))
            number_start = number_match.start()
            number_end = number_match.end()
            prefix = source_value[:number_start]
            suffix = source_value[number_end:]
        else:
            # No number in text, append number
            base_number = 0
            prefix = source_value
            suffix = ""
        
        # Get source position
        source_pos = source_text.GetPosition()
        
        # Create duplicates
        for i in range(1, count + 1):
            # Calculate new number
            new_number = base_number + (i * increment)
            
            # Create new text
            new_text = pcbnew.PCB_TEXT(board)
            
            # Set properties from source
            new_text.SetText(f"{prefix}{new_number}{suffix}")
            new_text.SetLayer(source_text.GetLayer())
            new_text.SetTextSize(source_text.GetTextSize())
            new_text.SetTextThickness(source_text.GetTextThickness())
            new_text.SetItalic(source_text.IsItalic())
            new_text.SetBold(source_text.IsBold())
            new_text.SetTextAngle(source_text.GetTextAngle())
            new_text.SetHorizJustify(source_text.GetHorizJustify())
            new_text.SetVertJustify(source_text.GetVertJustify())
            new_text.SetMirrored(source_text.IsMirrored())
            
            # Calculate new position
            new_x = source_pos.x + int(offset_x * i * 1000000)  # Convert mm to internal units
            new_y = source_pos.y + int(offset_y * i * 1000000)  # Convert mm to internal units
            new_text.SetPosition(pcbnew.VECTOR2I(new_x, new_y))
            
            # Add to board
            board.Add(new_text)
