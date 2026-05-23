#!/usr/bin/env python3
"""
Viral Neural Pepe Image Creator
Creates an eye-catching, meme-worthy Neural Pepe image
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

def create_viral_neural_pepe():
    # Create a 512x512 canvas
    size = 512
    img = Image.new('RGBA', (size, size), (10, 5, 30, 255))  # Deep purple background
    draw = ImageDraw.Draw(img)
    
    # Create gradient background effect
    for i in range(size):
        alpha = int(255 * (1 - i/size * 0.3))
        color = (10 + i//20, 5 + i//30, 30 + i//15, alpha)
        draw.line([(0, i), (size, i)], fill=color)
    
    # Draw Pepe-like frog shape (simplified)
    center_x, center_y = size // 2, size // 2 - 30
    
    # Frog body outline
    body_points = [
        (center_x - 120, center_y - 80),
        (center_x - 100, center_y - 120),
        (center_x - 60, center_y - 140),
        (center_x - 20, center_y - 130),
        (center_x + 20, center_y - 130),
        (center_x + 60, center_y - 140),
        (center_x + 100, center_y - 120),
        (center_x + 120, center_y - 80),
        (center_x + 110, center_y - 20),
        (center_x + 80, center_y + 40),
        (center_x + 40, center_y + 80),
        (center_x - 40, center_y + 80),
        (center_x - 80, center_y + 40),
        (center_x - 110, center_y - 20),
    ]
    
    # Fill body with gradient green
    for i in range(len(body_points) - 1):
        draw.polygon([body_points[i], body_points[i+1], (center_x, center_y)], 
                    fill=(50, 200, 100, 200), outline=(100, 255, 150, 255), width=3)
    
    # Eyes (glowing AI eyes)
    # Left eye
    left_eye_x, left_eye_y = center_x - 40, center_y - 40
    for radius in [25, 20, 15, 10, 5]:
        glow_intensity = 255 - (radius * 8)
        draw.ellipse([left_eye_x-radius, left_eye_y-radius, 
                     left_eye_x+radius, left_eye_y+radius], 
                    fill=(glow_intensity, glow_intensity, 255, min(255, glow_intensity)))
    draw.ellipse([left_eye_x-8, left_eye_y-8, left_eye_x+8, left_eye_y+8], 
                fill=(255, 255, 255, 255))
    
    # Right eye
    right_eye_x, right_eye_y = center_x + 40, center_y - 40
    for radius in [25, 20, 15, 10, 5]:
        glow_intensity = 255 - (radius * 8)
        draw.ellipse([right_eye_x-radius, right_eye_y-radius, 
                     right_eye_x+radius, right_eye_y+radius], 
                    fill=(glow_intensity, glow_intensity, 255, min(255, glow_intensity)))
    draw.ellipse([right_eye_x-8, right_eye_y-8, right_eye_x+8, right_eye_y+8], 
                fill=(255, 255, 255, 255))
    
    # Neural network overlay
    neural_nodes = []
    for i in range(25):
        x = random.randint(30, size-30)
        y = random.randint(30, size-30)
        neural_nodes.append((x, y))
    
    # Draw neural connections with glow effect
    for i, node1 in enumerate(neural_nodes):
        for node2 in neural_nodes[i+1:]:
            distance = math.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)
            if distance < 120:
                # Multi-layer glow for neural pathways
                for width, alpha in [(4, 30), (3, 50), (2, 80), (1, 120)]:
                    color = (0, 255, 200, alpha)
                    draw.line([node1, node2], fill=color, width=width)
    
    # Draw neural nodes
    for x, y in neural_nodes:
        # Pulsing effect nodes
        for radius in [8, 5, 3]:
            alpha = 200 - (radius * 20)
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                        fill=(0, 255, 255, alpha))
        draw.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255, 255))
    
    # Circuit board patterns
    for _ in range(8):
        x = random.randint(50, size-50)
        y = random.randint(50, size-50)
        width = random.randint(20, 60)
        height = random.randint(3, 8)
        draw.rectangle([x, y, x+width, y+height], 
                      fill=(100, 200, 255, 80), outline=(0, 255, 255, 150))
    
    # Add "AIPEPE" text with effects
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 56)
    except:
        font = ImageFont.load_default()
    
    text = "AIPEPE"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = size - 100
    
    # Text glow effect
    for offset in [(4, 4), (3, 3), (2, 2), (1, 1)]:
        alpha = 100 - (offset[0] * 20)
        draw.text((x+offset[0], y+offset[1]), text, font=font, 
                 fill=(0, 255, 255, alpha))
    
    # Main text with gradient effect
    draw.text((x, y), text, font=font, fill=(0, 255, 255, 255))
    draw.text((x+1, y), text, font=font, fill=(255, 255, 255, 200))
    
    # Add some sparkles for viral appeal
    for _ in range(20):
        x = random.randint(20, size-20)
        y = random.randint(20, size-20)
        size_sparkle = random.randint(2, 6)
        draw.ellipse([x-size_sparkle, y-size_sparkle, x+size_sparkle, y+size_sparkle], 
                    fill=(255, 255, 255, random.randint(100, 255)))
    
    # Apply slight blur for glow effect
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Save the image
    img.save('neural_pepe_viral.png')
    print("✅ VIRAL Neural Pepe image created as 'neural_pepe_viral.png'")
    print("📍 Location: /Users/sandhya/CascadeProjects/sahara/neural_pepe_viral.png")
    print("🚀 This image is designed to go viral! 🐸🤖")

if __name__ == "__main__":
    create_viral_neural_pepe()
