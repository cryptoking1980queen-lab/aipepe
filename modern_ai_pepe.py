#!/usr/bin/env python3
"""
Modern AI + Pepe Logo - Clean Professional Design
Creates a minimalist, sophisticated logo that appeals to serious investors
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import colorsys

def create_modern_ai_pepe():
    # Create clean canvas
    size = 1024
    img = Image.new('RGBA', (size, size), (255, 255, 255, 255))  # Pure white
    draw = ImageDraw.Draw(img)
    
    # Create subtle gradient background
    for y in range(size):
        for x in range(size):
            center_x, center_y = size // 2, size // 2
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx*dx + dy*dy)
            max_distance = math.sqrt(center_x*center_x + center_y*center_y)
            
            gradient_factor = min(1.0, distance / max_distance)
            
            # Very subtle white to light gray gradient
            gray_value = int(255 - gradient_factor * 15)
            img.putpixel((x, y), (gray_value, gray_value, gray_value, 255))
    
    # Create modern circular logo container
    center_x, center_y = size // 2, size // 2
    logo_radius = 300
    
    # White circle background
    draw.ellipse([center_x - logo_radius, center_y - logo_radius,
                  center_x + logo_radius, center_y + logo_radius],
                 fill=(255, 255, 255, 255), outline=(240, 240, 240, 255), width=3)
    
    # Inner circle for depth
    inner_radius = logo_radius - 20
    draw.ellipse([center_x - inner_radius, center_y - inner_radius,
                  center_x + inner_radius, center_y + inner_radius],
                 fill=(248, 248, 248, 255))
    
    # Create stylized Pepe face (minimalist)
    pepe_y = center_y + 30
    
    # Simple, clean Pepe head shape
    pepe_head = [
        (center_x - 180, pepe_y - 120),   # Left top
        (center_x - 160, pepe_y - 160),   # Left top-mid
        (center_x - 100, pepe_y - 180),   # Left-mid top
        (center_x - 40, pepe_y - 170),    # Left-center top
        (center_x + 40, pepe_y - 170),    # Right-center top
        (center_x + 100, pepe_y - 180),   # Right-mid top
        (center_x + 160, pepe_y - 160),   # Right top-mid
        (center_x + 180, pepe_y - 120),   # Right top
        (center_x + 170, pepe_y - 60),    # Right upper-mid
        (center_x + 140, pepe_y),         # Right mid
        (center_x + 120, pepe_y + 60),    # Right lower-mid
        (center_x + 80, pepe_y + 100),    # Right bottom
        (center_x - 80, pepe_y + 100),    # Left bottom
        (center_x - 120, pepe_y + 60),    # Left lower-mid
        (center_x - 140, pepe_y),         # Left mid
        (center_x - 170, pepe_y - 60),    # Left upper-mid
    ]
    
    # Fill Pepe head with modern green
    draw.polygon(pepe_head, fill=(46, 213, 115, 255), outline=(34, 197, 94, 255), width=2)
    
    # Modern, minimalist eyes
    eye_y = pepe_y - 40
    left_eye_x = center_x - 60
    right_eye_x = center_x + 60
    
    # Clean, circular eyes
    eye_radius = 25
    draw.ellipse([left_eye_x - eye_radius, eye_y - eye_radius,
                  left_eye_x + eye_radius, eye_y + eye_radius],
                 fill=(255, 255, 255, 255), outline=(34, 197, 94, 255), width=3)
    draw.ellipse([right_eye_x - eye_radius, eye_y - eye_radius,
                  right_eye_x + eye_radius, eye_y + eye_radius],
                 fill=(255, 255, 255, 255), outline=(34, 197, 94, 255), width=3)
    
    # Pupils
    pupil_radius = 12
    draw.ellipse([left_eye_x - pupil_radius, eye_y - pupil_radius,
                  left_eye_x + pupil_radius, eye_y + pupil_radius],
                 fill=(0, 0, 0, 255))
    draw.ellipse([right_eye_x - pupil_radius, eye_y - pupil_radius,
                  right_eye_x + pupil_radius, eye_y + pupil_radius],
                 fill=(0, 0, 0, 255))
    
    # Eye highlights (modern touch)
    highlight_radius = 4
    draw.ellipse([left_eye_x - 6, eye_y - 8, left_eye_x + 2, eye_y - 2],
                 fill=(255, 255, 255, 255))
    draw.ellipse([right_eye_x - 6, eye_y - 8, right_eye_x + 2, eye_y - 2],
                 fill=(255, 255, 255, 255))
    
    # Simple mouth
    mouth_y = pepe_y + 40
    mouth_width = 80
    mouth_height = 20
    
    # Subtle smile
    draw.arc([center_x - mouth_width, mouth_y - mouth_height,
              center_x + mouth_width, mouth_y + mouth_height],
             start=0, end=180, fill=(34, 197, 94, 255), width=3)
    
    # Enhanced AI brain circuit overlay
    brain_y = pepe_y - 140
    
    # Complex AI circuit pattern
    circuit_points = [
        (center_x - 120, brain_y),
        (center_x - 80, brain_y - 40),
        (center_x - 40, brain_y - 35),
        (center_x, brain_y - 45),
        (center_x + 40, brain_y - 35),
        (center_x + 80, brain_y - 40),
        (center_x + 120, brain_y),
    ]
    
    # Additional AI neural nodes
    neural_nodes = [
        (center_x - 60, brain_y - 20),
        (center_x - 20, brain_y - 10),
        (center_x + 20, brain_y - 10),
        (center_x + 60, brain_y - 20),
    ]
    
    # Draw main circuit connections
    for i in range(len(circuit_points) - 1):
        draw.line([circuit_points[i], circuit_points[i+1]], 
                 fill=(59, 130, 246, 220), width=5)
    
    # Draw neural connections to main circuit
    for neural_x, neural_y in neural_nodes:
        # Find closest circuit points
        closest_circuit = min(circuit_points, 
                            key=lambda p: math.sqrt((p[0]-neural_x)**2 + (p[1]-neural_y)**2))
        draw.line([neural_x, neural_y, closest_circuit[0], closest_circuit[1]], 
                 fill=(99, 102, 241, 180), width=3)
    
    # Main circuit nodes
    for x, y in circuit_points:
        # Outer glow
        draw.ellipse([x-12, y-12, x+12, y+12], fill=(59, 130, 246, 80))
        # Main node
        draw.ellipse([x-8, y-8, x+8, y+8], fill=(59, 130, 246, 255))
        # Inner core
        draw.ellipse([x-4, y-4, x+4, y+4], fill=(255, 255, 255, 255))
    
    # Neural nodes
    for x, y in neural_nodes:
        draw.ellipse([x-6, y-6, x+6, y+6], fill=(99, 102, 241, 200))
        draw.ellipse([x-3, y-3, x+3, y+3], fill=(255, 255, 255, 255))
    
    # Add AI data streams (subtle animated effect simulation)
    for i in range(8):
        angle = i * 45  # degrees
        rad = math.radians(angle)
        
        # Data stream from brain to Pepe
        start_x = center_x + 100 * math.cos(rad)
        start_y = brain_y + 20 * math.sin(rad)
        end_x = center_x + 60 * math.cos(rad)
        end_y = pepe_y - 60
        
        # Draw data stream particles
        for j in range(5):
            t = j / 5
            x = start_x + (end_x - start_x) * t
            y = start_y + (end_y - start_y) * t
            
            # Pulsing effect
            pulse = abs(math.sin(t * math.pi))
            size = 2 + pulse * 2
            alpha = int(100 + pulse * 100)
            
            draw.ellipse([x-size, y-size, x+size, y+size], 
                        fill=(139, 92, 246, alpha))
    
    # Add AI processing rings around the brain
    for ring_radius in [160, 180, 200]:
        # Draw dashed ring
        dash_length = 10
        gap_length = 5
        circumference = 2 * math.pi * ring_radius
        num_dashes = int(circumference / (dash_length + gap_length))
        
        for i in range(num_dashes):
            angle = (i * 2 * math.pi) / num_dashes
            start_angle = angle
            end_angle = angle + (dash_length * 2 * math.pi) / circumference
            
            # Calculate dash positions
            x1 = center_x + ring_radius * math.cos(start_angle)
            y1 = brain_y + ring_radius * math.sin(start_angle)
            x2 = center_x + ring_radius * math.cos(end_angle)
            y2 = brain_y + ring_radius * math.sin(end_angle)
            
            # Draw dash
            draw.line([x1, y1, x2, y2], fill=(59, 130, 246, 120), width=2)
    
    # Add crown-like structure above the AI brain
    crown_base_y = brain_y - 60
    crown_center_x = center_x
    
    # Crown base (foundation)
    crown_base_width = 140
    crown_base_height = 15
    draw.rectangle([crown_center_x - crown_base_width//2, crown_base_y,
                    crown_center_x + crown_base_width//2, crown_base_y + crown_base_height],
                   fill=(255, 215, 0, 255), outline=(218, 165, 32, 255), width=2)
    
    # Crown points (5 peaks)
    crown_points = []
    crown_peak_heights = [40, 50, 60, 50, 40]  # Central peak is tallest
    
    for i, height in enumerate(crown_peak_heights):
        x_offset = -60 + i * 30  # Spread across crown base
        peak_x = crown_center_x + x_offset
        peak_y = crown_base_y - height
        
        # Draw crown peak
        peak_points = [
            (peak_x - 15, crown_base_y),
            (peak_x, peak_y),
            (peak_x + 15, crown_base_y)
        ]
        draw.polygon(peak_points, fill=(255, 215, 0, 255), outline=(218, 165, 32, 255), width=2)
        
        # Add gem/jewel at each peak
        jewel_radius = 6
        jewel_colors = [
            (255, 0, 0, 255),    # Ruby - left
            (0, 255, 0, 255),    # Emerald - left-mid
            (0, 0, 255, 255),    # Sapphire - center
            (255, 255, 0, 255),  # Topaz - right-mid
            (255, 0, 255, 255),  # Amethyst - right
        ]
        
        jewel_color = jewel_colors[i]
        draw.ellipse([peak_x - jewel_radius, peak_y - jewel_radius,
                      peak_x + jewel_radius, peak_y + jewel_radius],
                     fill=jewel_color, outline=(255, 255, 255, 255), width=1)
        
        # Add sparkle effect to jewels
        for sparkle_offset in [(2, -2), (-2, 2)]:
            sparkle_x = peak_x + sparkle_offset[0]
            sparkle_y = peak_y + sparkle_offset[1]
            draw.ellipse([sparkle_x-1, sparkle_y-1, sparkle_x+1, sparkle_y+1],
                        fill=(255, 255, 255, 255))
    
    # Crown cross/arch at top (regal element)
    cross_width = 8
    cross_height = 20
    cross_x = crown_center_x
    cross_y = crown_base_y - 80  # Above tallest peak
    
    # Vertical part of cross
    draw.rectangle([cross_x - cross_width//2, cross_y - cross_height//2,
                    cross_x + cross_width//2, cross_y + cross_height//2],
                   fill=(255, 215, 0, 255), outline=(218, 165, 32, 255), width=1)
    
    # Horizontal part of cross
    draw.rectangle([cross_x - cross_height//2, cross_y - cross_width//2,
                    cross_x + cross_height//2, cross_y + cross_width//2],
                   fill=(255, 215, 0, 255), outline=(218, 165, 32, 255), width=1)
    
    # Add crown glow effect
    crown_glow_img = Image.new('RGBA', (int(size), int(size)), (0, 0, 0, 0))
    crown_glow_draw = ImageDraw.Draw(crown_glow_img)
    
    # Soft glow around crown
    crown_glow_draw.ellipse([int(crown_center_x - 100), int(crown_base_y - 100),
                             int(crown_center_x + 100), int(crown_base_y + 40)],
                            fill=(255, 215, 0, 30))
    
    # Blur and composite the glow
    crown_glow_img = crown_glow_img.filter(ImageFilter.GaussianBlur(radius=10))
    
    # Ensure sizes match before compositing
    if img.size == crown_glow_img.size:
        img = Image.alpha_composite(img, crown_glow_img)
    else:
        crown_glow_resized = crown_glow_img.resize(img.size, Image.Resampling.LANCZOS)
        img = Image.alpha_composite(img, crown_glow_resized)
    
    # Add subtle AI circuit connections to crown
    for i in range(3):
        angle = i * 120  # degrees
        rad = math.radians(angle)
        
        # Connect from AI brain to crown base
        start_x = center_x + 40 * math.cos(rad)
        start_y = brain_y
        end_x = crown_center_x + 50 * math.cos(rad)
        end_y = crown_base_y + crown_base_height//2
        
        # Draw connection
        draw.line([start_x, start_y, end_x, end_y], 
                 fill=(59, 130, 246, 150), width=2)
        
        # Add connection node at crown base
        draw.ellipse([end_x-4, end_y-4, end_x+4, end_y+4], 
                    fill=(59, 130, 246, 200))
    
    # Neural connections from brain to Pepe
    for i, (brain_x, brain_y) in enumerate(circuit_points):
        if i % 2 == 0:  # Connect every other node
            # Subtle neural lines
            pepe_connect_x = center_x + (brain_x - center_x) * 0.7
            pepe_connect_y = pepe_y - 80
            
            # Gradient line
            for j in range(10):
                t = j / 10
                x = brain_x + (pepe_connect_x - brain_x) * t
                y = brain_y + (pepe_connect_y - brain_y) * t
                
                # Color transition from blue to green
                blue_factor = 1 - t
                green_factor = t
                
                r = int(59 * blue_factor + 46 * green_factor)
                g = int(130 * blue_factor + 213 * green_factor)
                b = int(246 * blue_factor + 115 * green_factor)
                
                draw.ellipse([x-2, y-2, x+2, y+2], fill=(r, g, b, 150))
    
    # Modern typography
    try:
        # Try modern fonts
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/San Francisco.ttf",
        ]
        font = None
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, 80)
                break
            except:
                continue
        if not font:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Clean text layout
    text_y = center_y + 220
    
    # AI text
    ai_text = "AI"
    ai_bbox = draw.textbbox((0, 0), ai_text, font=font)
    ai_width = ai_bbox[2] - ai_bbox[0]
    ai_x = center_x - ai_width - 30
    
    draw.text((ai_x, text_y), ai_text, font=font, fill=(59, 130, 246, 255))
    
    # PEPE text
    pepe_text = "PEPE"
    pepe_bbox = draw.textbbox((0, 0), pepe_text, font=font)
    pepe_width = pepe_bbox[2] - pepe_bbox[0]
    pepe_x = center_x + 30
    
    draw.text((pepe_x, text_y), pepe_text, font=font, fill=(46, 213, 115, 255))
    
    # Subtle connection dot
    draw.ellipse([center_x-5, text_y+25, center_x+5, text_y+35], 
                 fill=(147, 51, 234, 200))
    
    # Apply subtle shadow effect
    shadow_img = Image.new('RGBA', (int(size), int(size)), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    
    # Soft shadow for the logo circle
    shadow_offset = 8
    shadow_blur = 20
    
    shadow_draw.ellipse([int(center_x - logo_radius + shadow_offset - shadow_blur),
                         int(center_y - logo_radius + shadow_offset - shadow_blur),
                         int(center_x + logo_radius + shadow_offset + shadow_blur),
                         int(center_y + logo_radius + shadow_offset + shadow_blur)],
                        fill=(0, 0, 0, 30))
    
    # Blur the shadow
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=int(shadow_blur)))
    
    # Composite shadow
    if img.size == shadow_img.size:
        img = Image.alpha_composite(img.convert('RGBA'), shadow_img)
    else:
        # Resize shadow to match img
        shadow_resized = shadow_img.resize(img.size, Image.Resampling.LANCZOS)
        img = Image.alpha_composite(img.convert('RGBA'), shadow_resized)
    
    # Final enhancements
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.05)
    
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.02)
    
    # Create final versions
    img_1024 = img.copy()
    img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    
    # Save versions
    img_1024.save('modern_ai_pepe_1024.png', 'PNG', optimize=True, quality=95)
    img_512.save('modern_ai_pepe.png', 'PNG', optimize=True, quality=95)
    
    print("✅ Modern AI + Pepe Logo created")
    print("📍 1024x1024: modern_ai_pepe_1024.png")
    print("📍 512x512: modern_ai_pepe.png")
    print("🎨 Clean, professional design complete!")
    
    return img_512

if __name__ == "__main__":
    create_modern_ai_pepe()
