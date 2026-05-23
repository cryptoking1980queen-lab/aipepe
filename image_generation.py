#!/usr/bin/env python3
"""
Neural Pepe Image Generator
Uses various AI image generation APIs to create the perfect meme coin image
"""

import requests
import json
import os
from typing import Optional

class NeuralPepeImageGenerator:
    def __init__(self):
        self.prompts = {
            "midjourney": "Pepe the Frog with glowing blue neural network patterns, circuit board textures on skin, glowing AI eyes, cyberpunk aesthetic, digital art, high resolution, square format, cryptocurrency meme coin style --ar 1:1",
            "dalle": "Create a square format image of Pepe the Frog transformed with artificial intelligence - glowing neural network patterns across his body, circuit board textures, bright blue AI eyes, cyberpunk colors, professional meme coin design",
            "stable_diffusion": "AI Pepe meme, Pepe the Frog with neural network patterns, glowing circuits, artificial intelligence eyes, futuristic, cryptocurrency theme, high quality digital art, 1:1 aspect ratio"
        }
    
    def generate_with_openai(self, api_key: str) -> Optional[str]:
        """Generate image using DALL-E 3"""
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "dall-e-3",
            "prompt": self.prompts["dalle"],
            "size": "1024x1024",
            "quality": "standard",
            "n": 1
        }
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["data"][0]["url"]
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Exception: {e}")
            return None
    
    def save_image_from_url(self, image_url: str, filename: str = "neural_pepe.png") -> bool:
        """Download and save image from URL"""
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Image saved as {filename}")
                return True
            else:
                print(f"Failed to download image: {response.status_code}")
                return False
        except Exception as e:
            print(f"Error saving image: {e}")
            return False
    
    def display_prompts(self):
        """Display all available prompts"""
        print("=== Neural Pepe Image Generation Prompts ===\n")
        for platform, prompt in self.prompts.items():
            print(f"{platform.upper()}:")
            print(f'"{prompt}"\n')

def main():
    generator = NeuralPepeImageGenerator()
    
    print("🐸 Neural Pepe Image Generator 🤖")
    print("=" * 50)
    
    # Display prompts
    generator.display_prompts()
    
    # Get user choice
    print("\nOptions:")
    print("1. Use DALL-E 3 (requires OpenAI API key)")
    print("2. Display prompts for manual use")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        api_key = input("Enter your OpenAI API key: ").strip()
        if api_key:
            print("Generating image with DALL-E 3...")
            image_url = generator.generate_with_openai(api_key)
            if image_url:
                print(f"Image generated! URL: {image_url}")
                if generator.save_image_from_url(image_url):
                    print("✅ Image saved as 'neural_pepe.png'")
            else:
                print("❌ Failed to generate image")
        else:
            print("❌ No API key provided")
    
    elif choice == "2":
        print("\nCopy these prompts for your preferred AI image generator:")
        generator.display_prompts()
    
    elif choice == "3":
        print("Good luck with Neural Pepe! 🚀")
    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
