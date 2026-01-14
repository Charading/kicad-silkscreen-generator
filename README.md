# KiCad Silkscreen Label Generator Plugin

A KiCad PCB Editor plugin that automates the creation of incremental silkscreen labels for pin headers and other components.

## Features

- 🔢 **Automatic Number Incrementing**: Automatically increments numbers in silkscreen labels (e.g., HE0 → HE1 → HE2)
- 📏 **Custom Offsets**: Set X and Y offset values for precise label positioning
- 🎯 **Flexible Increment Values**: Choose any increment value (1, 2, 5, 10, etc.)
- 🔄 **Batch Generation**: Create multiple labels at once (up to 1000)
- 💡 **Smart Text Handling**: Works with or without existing numbers in labels

## Use Cases

Perfect for:
- Pin headers (2.54mm pitch)
- Terminal blocks
- Connector labels
- Test points
- Any repeated labeling tasks

## Installation

### Windows

1. Find your KiCad plugins directory:
   - Usually: `C:\Users\[YourUsername]\Documents\KiCad\[version]\scripting\plugins\`
   - Or: `%APPDATA%\kicad\[version]\scripting\plugins\`

2. Copy the entire `kicad-silkscreen-generator` folder to the plugins directory

3. Restart KiCad PCB Editor

### Linux

1. Copy to: `~/.kicad/scripting/plugins/`
2. Restart KiCad PCB Editor

### macOS

1. Copy to: `~/Library/Application Support/kicad/scripting/plugins/`
2. Restart KiCad PCB Editor

## Usage

### Step 1: Create or Select a Silkscreen Label

1. Open your PCB in KiCad PCB Editor
2. Add a silkscreen text label (or select an existing one)
   - Example: "HE0" for a header starting at pin 0
   - Or: "PIN1" for a pin starting at 1
   - Or even: "HEADER" (plugin will add numbers automatically)

### Step 2: Run the Plugin

1. Select the silkscreen label you want to duplicate
2. Click on **Tools → External Plugins → Silkscreen Label Generator**
   - Or find it in the toolbar if enabled

### Step 3: Configure Parameters

The dialog will show your selected label and these options:

- **Number of Copies**: How many labels to generate (default: 10)
- **Number Increment**: How much to increment each number (default: 1)
- **X Offset (mm)**: Horizontal spacing between labels (default: 0.0)
- **Y Offset (mm)**: Vertical spacing between labels (default: 2.54)

### Step 4: Generate

Click **Generate** and the plugin will create all your labels!

## Examples

### Example 1: Vertical Pin Header (2.54mm pitch)

- Select label: "PIN1"
- Number of Copies: 10
- Number Increment: 1
- X Offset: 0.0 mm
- Y Offset: 2.54 mm

**Result**: PIN1, PIN2, PIN3... PIN11 spaced 2.54mm apart vertically

### Example 2: Horizontal Header

- Select label: "A0"
- Number of Copies: 8
- Number Increment: 1
- X Offset: 2.54 mm
- Y Offset: 0.0 mm

**Result**: A0, A1, A2... A8 spaced 2.54mm apart horizontally

### Example 3: Even Numbers Only

- Select label: "D0"
- Number of Copies: 5
- Number Increment: 2
- X Offset: 0.0 mm
- Y Offset: 2.0 mm

**Result**: D0, D2, D4, D6, D8, D10

### Example 4: Starting Mid-Sequence

- Select label: "HE11" (continuing from previous header)
- Number of Copies: 10
- Number Increment: 1
- X Offset: 0.0 mm
- Y Offset: 2.54 mm

**Result**: HE12, HE13, HE14... HE21

### Example 5: No Initial Number

- Select label: "HEADER"
- Number of Copies: 5
- Number Increment: 1
- X Offset: 0.0 mm
- Y Offset: 2.54 mm

**Result**: HEADER1, HEADER2, HEADER3, HEADER4, HEADER5

## Tips

- The original selected label is **not** modified
- All generated labels inherit properties from the source (font size, layer, style, etc.)
- Labels are added to the same silkscreen layer as the source
- You can use negative offsets to generate labels in the opposite direction
- Use X and Y offsets together for diagonal arrangements

## Troubleshooting

**Plugin doesn't appear in menu:**
- Make sure you copied the entire folder to the correct plugins directory
- Restart KiCad completely
- Check KiCad → Preferences → Configure Paths to verify plugin location

**"No Selection" error:**
- You must select exactly one silkscreen text object before running the plugin
- Make sure you're selecting a text object, not a footprint or other item

**Labels appear in wrong location:**
- Check your offset units (they're in millimeters)
- Try negative values if labels go the wrong direction
- Verify the selected text is where you expect it to be

## Requirements

- KiCad 6.0 or later (tested with KiCad 7.0+)
- Python 3.x (included with KiCad)
- wxPython (included with KiCad)

## License

MIT License - Feel free to modify and distribute

## Contributing

Suggestions and improvements welcome! This plugin was created to streamline repetitive PCB labeling tasks.

## Version History

- **1.0.0** - Initial release
  - Basic label duplication and incrementing
  - GUI dialog for parameter input
  - Support for X and Y offsets
  - Flexible increment values
