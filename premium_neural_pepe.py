#!/usr/bin/env python3
"""
Premium Neural Pepe Image Creator
Creates a professional, high-quality meme coin image that rivals top projects
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import random
import math
import colorsys

def create_premium_neural_pepe():
    # Create a 1024x1024 canvas for high quality
    size = 1024
    img = Image.new('RGBA', (size, size), (15, 10, 40, 255))  # Deep space background
    draw = ImageDraw.Draw(img)
    
    # Create sophisticated gradient background
    for y in range(size):
        # Create radial gradient from center
        center_dist = math.sqrt((size//2)**2 + (y - size//2)**2)
        gradient_factor = min(1.0, center_dist / (size//2))
        
        # Multi-tone gradient
        r = int(15 + gradient_factor * 20)
        g = int(10 + gradient_factor * 30)
        b = int(40 + gradient_factor * 60)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    # Add subtle grid pattern for tech feel
    grid_spacing = 40
    for x in range(0, size, grid_spacing):
        draw.line([(x, 0), (x, size)], fill=(30, 25, 60, 50), width=1)
    for y in range(0, size, grid_spacing):
        draw.line([(0, y), (size, y)], fill=(30, 25, 60, 50), width=1)
    
    # Create premium Pepe design
    center_x, center_y = size // 2, size // 2
    
    # Pepe head shape (more refined)
    head_scale = 1.8
    head_points = []
    
    # Generate smooth Pepe head outline
    for angle in range(0, 360, 5):
        rad = math.radians(angle)
        # Create Pepe-like shape with variations
        base_radius = 200 * head_scale
        
        if -90 <= angle <= 90:  # Top part (wider)
            radius = base_radius * 1.2
        elif 90 < angle <= 180:  # Right side
            radius = base_radius * 0.9
        else:  # Left side
            radius = base_radius * 0.9
            
        # Add some organic variation
        radius += math.sin(angle * 0.1) * 20
        
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad) * 0.8  # Slightly compressed
        head_points.append((x, y))
    
    # Draw Pepe head with gradient fill
    head_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    head_draw = ImageDraw.Draw(head_img)
    
    # Create gradient for Pepe head
    for i, point in enumerate(head_points):
        next_point = head_points[(i + 1) % len(head_points)]
        # Green gradient from light to dark
        green_intensity = 150 + int(50 * math.sin(i * 0.1))
        color = (50, green_intensity, 100, 200)
        head_draw.polygon([point, next_point, (center_x, center_y)], fill=color)
    
    # Blend head with main image
    img = Image.alpha_composite(img, head_img)
    
    # Create premium eyes with advanced glow
    eye_positions = [
        (center_x - 150, center_y - 100),  # Left eye
        (center_x + 150, center_y - 100)   # Right eye
    ]
    
    for eye_x, eye_y in eye_positions:
        # Multi-layer glow effect for eyes
        glow_colors = [
            (255, 100, 255, 30),   # Purple outer glow
            (100, 200, 255, 50),   # Blue middle glow
            (255, 255, 255, 80),   # White inner glow
        ]
        
        for i, (r, g, b, a) in enumerate(glow_colors):
            radius = 60 - i * 15
            # Create glow ellipse
            glow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_img)
            glow_draw.ellipse([eye_x-radius, eye_y-radius, eye_x+radius, eye_y+radius], 
                            fill=(r, g, b, a))
            img = Image.alpha_composite(img, glow_img)
        
        # Eye pupil
        pupil_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        pupil_draw = ImageDraw.Draw(pupil_img)
        
        # Outer iris ring
        pupil_draw.ellipse([eye_x-25, eye_y-25, eye_x+25, eye_y+25], 
                         fill=(0, 150, 255, 200))
        # Inner pupil
        pupil_draw.ellipse([eye_x-12, eye_y-12, eye_x+12, eye_y+12], 
                         fill=(0, 0, 0, 255))
        # Highlight
        pupil_draw.ellipse([eye_x-5, eye_y-8, eye_x+5, eye_y+2], 
                         fill=(255, 255, 255, 255))
        
        img = Image.alpha_composite(img, pupil_img)
    
    # Add sophisticated neural network
    neural_nodes = []
    for i in range(40):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(100, 400)
        x = center_x + distance * math.cos(angle)
        y = center_y + distance * math.sin(angle)
        neural_nodes.append((x, y))
    
    # Draw neural connections with gradient
    for i, node1 in enumerate(neural_nodes):
        for node2 in neural_nodes[i+1:]:
            distance = math.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)
            if distance < 200:
                # Create gradient line effect
                steps = 10
                for step in range(steps):
                    t = step / steps
                    x = node1[0] + (node2[0] - node1[0]) * t
                    y = node1[1] + (node2[1] - node1[1]) * t
                    
                    # Color gradient along the line
                    hue = (i + step) % 360 / 360
                    rgb = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
                    color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), 100)
                    
                    draw.ellipse([x-3, y-3, x+3, y+3], fill=color)
    
    # Draw neural nodes with pulsing effect
    for x, y in neural_nodes:
        # Outer glow
        for radius in [15, 10, 6]:
            alpha = 80 - radius * 4
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                        fill=(100, 200, 255, alpha))
        # Core
        draw.ellipse([x-3, y-3, x+3, y+3], fill=(255, 255, 255, 255))
    
    # Add circuit board elements
    circuit_elements = []
    for _ in range(15):
        x = random.randint(100, size-100)
        y = random.randint(100, size-100)
        width = random.randint(30, 100)
        height = random.randint(5, 15)
        circuit_elements.append((x, y, width, height))
        
        # Draw circuit with gradient
        for i in range(height):
            alpha = 100 - i * 5
            draw.rectangle([x, y+i, x+width, y+i+1], 
                         fill=(0, 255, 200, alpha))
    
    # Add premium text with advanced effects
    try:
        # Try to find a good font
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Verdana.ttf"
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
    
    text = "AIPEPE"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = size - 200
    
    # Create text with multiple effects
    text_layers = []
    
    # Shadow layers
    for offset, alpha in [(8, 40), (6, 60), (4, 80), (2, 100)]:
        shadow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_img)
        shadow_draw.text((x+offset, y+offset), text, font=font, fill=(0, 0, 0, alpha))
        text_layers.append(shadow_img)
    
    # Main text with gradient
    main_text_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    main_draw = ImageDraw.Draw(main_text_img)
    
    # Create gradient text effect
    for i in range(text_height):
        gradient_color = (
            int(0 + i * 2),
            int(200 + i * 0.5),
            int(255 - i * 0.5),
            255
        )
        # Draw text line by line for gradient
        main_draw.text((x, y+i), text, font=font, fill=gradient_color)
    
    text_layers.append(main_text_img)
    
    # Composite all text layers
    for text_layer in text_layers:
        img = Image.alpha_composite(img, text_layer)
    
    # Add holographic effect elements
    for _ in range(30):
        x = random.randint(50, size-50)
        y = random.randint(50, size-50)
        size_holo = random.randint(2, 8)
        
        # Holographic colors
        hue = random.random()
        rgb = colorsys.hsv_to_rgb(hue, 0.7, 1.0)
        color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), random.randint(100, 200))
        
        draw.ellipse([x-size_holo, y-size_holo, x+size_holo, y+size_holo], 
                    fill=color)
    
    # Apply final enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.1)
    
    # Resize to 512x512 for pump.fun
    img = img.resize((512, 512), Image.Resampling.LANCZOS)
    
    # Save the premium image
    img.save('neural_pepe_premium.png', 'PNG', optimize=True)
    print("✅ PREMIUM Neural Pepe image created as 'neural_pepe_premium.png'")
    print("📍 Location: /Users/sandhya/CascadeProjects/sahara/neural_pepe_premium.png")
    print("💎 This is professional-grade quality! 🚀🐸🤖")
    
    return img

if __name__ == "__main__":
    create_premium_neural_pepe()
