#!/usr/bin/env python3
"""
AI + Pepe Combo Logo Creator
Creates a perfect fusion of AI and Pepe elements in a cohesive design
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import colorsys

def create_ai_pepe_combo():
    # Create high-resolution canvas
    size = 1024
    img = Image.new('RGBA', (size, size), (15, 20, 45, 255))  # Deep tech blue
    draw = ImageDraw.Draw(img)
    
    # Create modern gradient background
    center_x, center_y = size // 2, size // 2
    
    for y in range(size):
        for x in range(size):
            # Calculate distance from center
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx*dx + dy*dy)
            max_distance = math.sqrt(center_x*center_x + center_y*center_y)
            
            # Create radial gradient
            gradient_factor = min(1.0, distance / max_distance)
            
            # Modern tech gradient (blue to purple)
            r = int(15 + gradient_factor * 25)
            g = int(20 + gradient_factor * 15)
            b = int(45 + gradient_factor * 35)
            
            img.putpixel((x, y), (r, g, b, 255))
    
    # Add subtle tech grid
    grid_spacing = 32
    grid_color = (40, 50, 80, 60)
    
    for x in range(0, size, grid_spacing):
        draw.line([(x, 0), (x, size)], fill=grid_color, width=1)
    for y in range(0, size, grid_spacing):
        draw.line([(0, y), (size, y)], fill=grid_color, width=1)
    
    # Create AI brain/halo effect
    brain_center_x, brain_center_y = center_x, center_y - 50
    
    # AI brain glow layers
    brain_colors = [
        (100, 200, 255, 20, 180),  # Outer blue
        (150, 100, 255, 25, 140),  # Middle purple
        (200, 150, 255, 30, 100),  # Inner lavender
        (255, 200, 255, 35, 60),   # Core pink
    ]
    
    for r, g, b, a, radius in brain_colors:
        brain_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        brain_draw = ImageDraw.Draw(brain_img)
        
        # Create glowing brain halo
        brain_draw.ellipse([brain_center_x-radius, brain_center_y-radius,
                           brain_center_x+radius, brain_center_y+radius],
                          fill=(r, g, b, a))
        img = Image.alpha_composite(img, brain_img)
    
    # Create Pepe face integrated with AI
    pepe_center_x, pepe_center_y = center_x, center_y + 50
    
    # Pepe face outline (clean, modern)
    pepe_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    pepe_draw = ImageDraw.Draw(pepe_img)
    
    # Modern Pepe head shape
    pepe_points = []
    for angle in range(0, 360, 3):
        rad = math.radians(angle)
        
        # Clean Pepe proportions
        if -45 <= angle <= 45:  # Forehead
            radius = 280
        elif 45 < angle <= 135:  # Right side
            radius = 250
        elif 135 < angle <= 180:  # Right jaw
            radius = 230
        elif -180 <= angle <= -135:  # Left jaw
            radius = 230
        elif -135 < angle <= -45:  # Left side
            radius = 250
        else:  # Chin
            radius = 220
            
        # Smooth organic variation
        radius += math.sin(angle * 0.08) * 10
        
        x = pepe_center_x + radius * math.cos(rad)
        y = pepe_center_y + radius * math.sin(rad) * 0.9  # Slightly compressed
        pepe_points.append((x, y))
    
    # Fill Pepe with modern green
    for i, point in enumerate(pepe_points):
        next_point = pepe_points[(i + 1) % len(pepe_points)]
        
        # Modern green gradient
        green_value = 140 + int(30 * math.sin(i * 0.03))
        color = (40, green_value, 80, 230)
        pepe_draw.polygon([point, next_point, (pepe_center_x, pepe_center_y)], fill=color)
    
    img = Image.alpha_composite(img, pepe_img)
    
    # AI + Pepe integrated eyes (the fusion point)
    eye_positions = [
        (pepe_center_x - 100, pepe_center_y - 80),  # Left eye
        (pepe_center_x + 100, pepe_center_y - 80)   # Right eye
    ]
    
    for eye_x, eye_y in eye_positions:
        # AI circuit patterns around eyes
        circuit_points = []
        for angle in range(0, 360, 30):
            rad = math.radians(angle)
            x = eye_x + 40 * math.cos(rad)
            y = eye_y + 40 * math.sin(rad)
            circuit_points.append((x, y))
        
        # Draw circuit connections
        for i, point in enumerate(circuit_points):
            next_point = circuit_points[(i + 1) % len(circuit_points)]
            draw.line([point, next_point], fill=(0, 255, 200, 100), width=2)
            
            # Circuit nodes
            draw.ellipse([point[0]-3, point[1]-3, point[0]+3, point[1]+3], 
                        fill=(0, 255, 255, 200))
        
        # AI-enhanced Pepe eyes
        eye_layers = [
            (0, 150, 255, 30, 50),   # Blue glow
            (150, 100, 255, 40, 35),  # Purple glow
            (255, 150, 255, 50, 25),  # Pink glow
        ]
        
        for r, g, b, a, radius in eye_layers:
            eye_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            eye_draw = ImageDraw.Draw(eye_img)
            eye_draw.ellipse([eye_x-radius, eye_y-radius, eye_x+radius, eye_y+radius],
                            fill=(r, g, b, a))
            img = Image.alpha_composite(img, eye_img)
        
        # Eye iris with AI pattern
        iris_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        iris_draw = ImageDraw.Draw(iris_img)
        
        # AI iris design
        iris_draw.ellipse([eye_x-25, eye_y-25, eye_x+25, eye_y+25],
                         fill=(20, 120, 200, 180))
        
        # AI neural pattern in iris
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = eye_x + 8 * math.cos(rad)
            y1 = eye_y + 8 * math.sin(rad)
            x2 = eye_x + 20 * math.cos(rad)
            y2 = eye_y + 20 * math.sin(rad)
            iris_draw.line([x1, y1, x2, y2], fill=(0, 255, 255, 150), width=1)
        
        # Pupil
        iris_draw.ellipse([eye_x-10, eye_y-10, eye_x+10, eye_y+10],
                         fill=(0, 0, 0, 255))
        
        # AI highlight
        iris_draw.ellipse([eye_x-4, eye_y-6, eye_x+4, eye_y+2],
                         fill=(255, 255, 255, 255))
        
        img = Image.alpha_composite(img, iris_img)
    
    # Neural network connecting AI brain to Pepe
    neural_start_points = []
    neural_end_points = []
    
    # Points from AI brain
    for angle in range(0, 360, 20):
        rad = math.radians(angle)
        x = brain_center_x + 150 * math.cos(rad)
        y = brain_center_y + 150 * math.sin(rad)
        neural_start_points.append((x, y))
    
    # Points to Pepe head
    for angle in range(0, 360, 25):
        rad = math.radians(angle)
        x = pepe_center_x + 200 * math.cos(rad)
        y = pepe_center_y + 200 * math.sin(rad)
        neural_end_points.append((x, y))
    
    # Draw neural connections
    for start in neural_start_points:
        for end in neural_end_points:
            distance = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
            if distance < 300:  # Only connect nearby points
                # Gradient neural connection
                steps = 20
                for step in range(steps):
                    t = step / steps
                    x = start[0] + (end[0] - start[0]) * t
                    y = start[1] + (end[1] - start[1]) * t
                    
                    # Color gradient from AI to Pepe
                    if t < 0.5:
                        # AI colors (blue/purple)
                        hue = 0.6 + t * 0.1
                    else:
                        # Pepe colors (green)
                        hue = 0.3 - (t - 0.5) * 0.1
                    
                    rgb = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
                    color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), 80)
                    
                    draw.ellipse([x-2, y-2, x+2, y+2], fill=color)
    
    # AI + Pepe text logo
    try:
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Arial.ttf",
        ]
        font = None
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, 120)
                break
            except:
                continue
        if not font:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Create AI text
    ai_text = "AI"
    ai_bbox = draw.textbbox((0, 0), ai_text, font=font)
    ai_width = ai_bbox[2] - ai_bbox[0]
    ai_x = center_x - ai_width - 20
    ai_y = 100
    
    # AI text with tech glow
    for offset, alpha in [(6, 40), (4, 60), (2, 80)]:
        draw.text((ai_x+offset, ai_y+offset), ai_text, font=font, fill=(0, 150, 255, alpha))
    draw.text((ai_x, ai_y), ai_text, font=font, fill=(100, 200, 255, 255))
    
    # Create Pepe text
    pepe_text = "PEPE"
    pepe_bbox = draw.textbbox((0, 0), pepe_text, font=font)
    pepe_width = pepe_bbox[2] - pepe_bbox[0]
    pepe_x = center_x + 20
    pepe_y = 100
    
    # Pepe text with meme glow
    for offset, alpha in [(6, 40), (4, 60), (2, 80)]:
        draw.text((pepe_x+offset, pepe_y+offset), pepe_text, font=font, fill=(0, 200, 100, alpha))
    draw.text((pepe_x, pepe_y), pepe_text, font=font, fill=(50, 220, 120, 255))
    
    # Connection symbol between AI and PEPE
    connection_x = center_x
    connection_y = 140
    
    # Neural bridge symbol
    for i in range(5):
        y = connection_y + i * 8
        alpha = 120 - i * 20
        draw.ellipse([connection_x-15, y-3, connection_x+15, y+3], 
                    fill=(200, 150, 255, alpha))
    
    # Final enhancements
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)
    
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.05)
    
    # Create final versions
    img_1024 = img.copy()
    img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    
    # Save versions
    img_1024.save('ai_pepe_combo_1024.png', 'PNG', optimize=True, quality=95)
    img_512.save('ai_pepe_combo.png', 'PNG', optimize=True, quality=95)
    
    print("✅ AI + Pepe Combo Logo created")
    print("📍 1024x1024: ai_pepe_combo_1024.png")
    print("📍 512x512: ai_pepe_combo.png")
    print("🤖🐸 Perfect fusion complete!")
    
    return img_512

if __name__ == "__main__":
    create_ai_pepe_combo()
