"""
GUI Dialog for Silkscreen Label Generator
"""

import wx
import pcbnew
import json
import os


class SilkscreenGeneratorDialog(wx.Dialog):
    def __init__(self, parent, source_text):
        super().__init__(
            parent,
            title="Silkscreen Label Generator",
            size=(450, 400)
        )
        
        self.source_text = source_text
        self.settings_file = os.path.join(os.path.dirname(__file__), 'settings.json')
        self.InitUI()
        self.LoadSettings()
        self.Centre()
    
    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Display source text
        source_label = wx.StaticText(panel, label=f"Source Label: {self.source_text.GetText()}")
        font = source_label.GetFont()
        font.PointSize += 1
        font = font.Bold()
        source_label.SetFont(font)
        vbox.Add(source_label, flag=wx.ALL | wx.EXPAND, border=10)
        
        # Add separator
        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add((-1, 10))
        
        # Create form
        fgs = wx.FlexGridSizer(4, 2, 10, 10)
        
        # Count
        count_label = wx.StaticText(panel, label="Number of Copies:")
        self.count_ctrl = wx.SpinCtrl(panel, value="10", min=1, max=1000)
        fgs.Add(count_label, flag=wx.ALIGN_CENTER_VERTICAL)
        fgs.Add(self.count_ctrl, flag=wx.EXPAND)
        
        # Increment
        increment_label = wx.StaticText(panel, label="Number Increment:")
        self.increment_ctrl = wx.SpinCtrl(panel, value="1", min=1, max=1000)
        fgs.Add(increment_label, flag=wx.ALIGN_CENTER_VERTICAL)
        fgs.Add(self.increment_ctrl, flag=wx.EXPAND)
        
        # X Offset
        x_offset_label = wx.StaticText(panel, label="X Offset (mm):")
        self.x_offset_ctrl = wx.TextCtrl(panel, value="0.0")
        fgs.Add(x_offset_label, flag=wx.ALIGN_CENTER_VERTICAL)
        fgs.Add(self.x_offset_ctrl, flag=wx.EXPAND)
        
        # Y Offset
        y_offset_label = wx.StaticText(panel, label="Y Offset (mm):")
        self.y_offset_ctrl = wx.TextCtrl(panel, value="2.54")
        fgs.Add(y_offset_label, flag=wx.ALIGN_CENTER_VERTICAL)
        fgs.Add(self.y_offset_ctrl, flag=wx.EXPAND)
        
        fgs.AddGrowableCol(1, 1)
        
        vbox.Add(fgs, flag=wx.ALL | wx.EXPAND, border=10)
        
        # Add info text
        info_text = wx.StaticText(
            panel,
            label="Tip: For vertical pin headers use Y offset (e.g., 2.54mm)\n"
                  "     For horizontal pin headers use X offset (e.g., 2.54mm)"
        )
        info_text.SetForegroundColour(wx.Colour(100, 100, 100))
        vbox.Add(info_text, flag=wx.ALL | wx.EXPAND, border=10)
        
        vbox.Add((-1, 10))
        
        # Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(panel, wx.ID_OK, "Generate")
        cancel_button = wx.Button(panel, wx.ID_CANCEL, "Cancel")
        hbox.Add(ok_button)
        hbox.Add(cancel_button, flag=wx.LEFT, border=5)
        
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        
        panel.SetSizer(vbox)
        
        # Bind validation
        ok_button.Bind(wx.EVT_BUTTON, self.OnOK)
    
    def OnOK(self, event):
        """Validate inputs before closing"""
        try:
            float(self.x_offset_ctrl.GetValue())
            float(self.y_offset_ctrl.GetValue())
        except ValueError:
            wx.MessageBox(
                "Please enter valid numbers for X and Y offsets!",
                "Invalid Input",
                wx.OK | wx.ICON_ERROR
            )
            return
        
        self.SaveSettings()
        event.Skip()
    
    def GetValues(self):
        """Return the values from the dialog"""
        return {
            'count': self.count_ctrl.GetValue(),
            'increment': self.increment_ctrl.GetValue(),
            'offset_x': float(self.x_offset_ctrl.GetValue()),
            'offset_y': float(self.y_offset_ctrl.GetValue())
        }
    
    def LoadSettings(self):
        """Load last used settings from file"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    settings = json.load(f)
                    self.count_ctrl.SetValue(settings.get('count', 10))
                    self.increment_ctrl.SetValue(settings.get('increment', 1))
                    self.x_offset_ctrl.SetValue(str(settings.get('offset_x', 0.0)))
                    self.y_offset_ctrl.SetValue(str(settings.get('offset_y', 2.54)))
        except Exception:
            pass  # Use defaults if loading fails
    
    def SaveSettings(self):
        """Save current settings to file"""
        try:
            settings = {
                'count': self.count_ctrl.GetValue(),
                'increment': self.increment_ctrl.GetValue(),
                'offset_x': float(self.x_offset_ctrl.GetValue()),
                'offset_y': float(self.y_offset_ctrl.GetValue())
            }
            with open(self.settings_file, 'w') as f:
                json.dump(settings, f, indent=2)
        except Exception:
            pass  # Silently fail if saving doesn't work
