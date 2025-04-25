from PIL import Image, ImageDraw, ImageFont
import solveitcore
import os

header_bg = "#B2BEC9" # 178, 190, 201 B2BEC9
cell_bg = "#E4EBEF" # E4EBEF
text_colour = "#111827"


def wrap_text(text, font, max_width, draw):
    """Break text into lines that fit within max_width."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        if line_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())
    return lines

def create_technique_box_wrapped(technique_id, description, output_path):
    width, height = 400, 200
    bg_color = cell_bg
    text_color = text_colour
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font_size = 32
    padding = 10
    line_spacing = 4

    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    # Wrap the description text
    max_text_width = width - 2 * padding
    lines = wrap_text(description, font, max_text_width, draw)

    # Compute total height for wrapped lines + technique ID
    text_heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_heights.append(bbox[3] - bbox[1])
    desc_total_height = sum(text_heights) + line_spacing * (len(lines) - 1)

    # Technique ID height
    id_bbox = draw.textbbox((0, 0), technique_id, font=font)
    id_height = id_bbox[3] - id_bbox[1]

    # Combined vertical centering
    total_height = desc_total_height + 10 + id_height
    start_y = (height - total_height) / 2

    # Draw wrapped description
    y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2
        draw.text((x, y), line, fill=text_color, font=font)
        y += bbox[3] - bbox[1] + line_spacing

    # Draw technique ID
    id_width = id_bbox[2] - id_bbox[0]
    id_x = (width - id_width) / 2
    draw.text((id_x, y + 10), technique_id, fill=text_color, font=font)

    img.save(output_path)

def create_single_label_box(text, output_path):
    # Image settings
    width, height = 400, 200
    bg_color = header_bg
    text_color = text_colour
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font_size = 32

    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Get bounding box of text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_w = text_bbox[2] - text_bbox[0]
    text_h = text_bbox[3] - text_bbox[1]

    # Center text both horizontally and vertically
    text_x = (width - text_w) / 2
    text_y = (height - text_h) / 2

    # Draw text
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Save image
    img.save(output_path)




if __name__ == "__main__":

    kb = solveitcore.SOLVEIT('../data')

    if not os.path.exists('images'):
        os.makedirs('images')

    for each_obj in kb.tactics:
        obj_name = each_obj.get('name')
        obj_path = os.path.join('images', obj_name)
        if not os.path.exists(obj_path):
            os.makedirs(obj_path)
        create_single_label_box(obj_name, f"{os.path.join(obj_path, obj_name)}.png")

        for each_technique_id in sorted(each_obj.get('techniques')):
            technique_name = kb.get_technique(each_technique_id).get('name')
            each_technique = kb.get_technique(each_technique_id)
            create_technique_box_wrapped(each_technique_id,
                                 technique_name,
                                 os.path.join(obj_path, f"{each_technique_id}.png"))


