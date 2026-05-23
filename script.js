// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    
    // Particle System
    function createParticles() {
        const particlesContainer = document.getElementById('particles');
        const aiEmojis = ['🤖', '🐸', '👑', '⚡', '🧠', '💎', '📈', '💹', '🔮', '✨', '💳', '🌟'];
        
        for (let i = 0; i < 8; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.textContent = aiEmojis[Math.floor(Math.random() * aiEmojis.length)];
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 20 + 's';
            particle.style.fontSize = (Math.random() * 15 + 12) + 'px';
            particlesContainer.appendChild(particle);
        }
    }
    
    // Mouse Glow Effect
    function initMouseGlow() {
        const mouseGlow = document.getElementById('mouseGlow');
        let mouseX = 0, mouseY = 0;
        let currentX = 0, currentY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            mouseGlow.classList.add('active');
        });
        
        document.addEventListener('mouseleave', () => {
            mouseGlow.classList.remove('active');
        });
        
        function animateGlow() {
            currentX += (mouseX - currentX) * 0.1;
            currentY += (mouseY - currentY) * 0.1;
            
            mouseGlow.style.left = currentX + 'px';
            mouseGlow.style.top = currentY + 'px';
            
            requestAnimationFrame(animateGlow);
        }
        
        animateGlow();
    }
    
    // Magnetic Button Effect
    function initMagneticButtons() {
        const buttons = document.querySelectorAll('.buy-button, .cta-button, .step-link');
        
        buttons.forEach(button => {
            button.addEventListener('mousemove', (e) => {
                const rect = button.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                button.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
            });
            
            button.addEventListener('mouseleave', () => {
                button.style.transform = 'translate(0, 0)';
            });
        });
    }
    
    // Copy Address Functionality
    function initCopyAddress() {
        const copyBtn = document.getElementById('copyBtn');
        const contractAddress = document.getElementById('contractAddress');
        const copyFeedback = copyBtn.querySelector('.copy-feedback');
        
        copyBtn.addEventListener('click', async () => {
            try {
                const address = contractAddress.textContent;
                await navigator.clipboard.writeText(address);
                
                // Show feedback
                copyFeedback.style.display = 'inline';
                copyBtn.style.background = 'rgba(46, 213, 115, 0.2)';
                
                // Hide feedback after 2 seconds
                setTimeout(() => {
                    copyFeedback.style.display = 'none';
                    copyBtn.style.background = 'rgba(255, 255, 255, 0.1)';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy address:', err);
            }
        });
    }
    
    // Smooth Scrolling
    function initSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                
                const targetId = link.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 80;
                    
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
    
    // Parallax Effect
    function initParallax() {
        const parallaxLayers = document.querySelectorAll('.parallax-layer');
        
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            
            parallaxLayers.forEach((layer, index) => {
                const speed = 0.5 + (index * 0.1);
                const yPos = -(scrolled * speed);
                
                layer.style.transform = `translateY(${yPos}px)`;
            });
        });
    }
    
    // Intersection Observer for Animations
    function initIntersectionObserver() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);
        
        // Observe elements
        const animatedElements = document.querySelectorAll('.ai-card, .step, .community-link');
        
        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }
    
    // Dynamic Gradient Background
    function initDynamicGradient() {
        const gradientBg = document.getElementById('gradientBg');
        let hue = 0;
        
        function updateGradient() {
            hue = (hue + 0.5) % 360;
            
            const color1 = `hsl(${hue}, 70%, 50%)`;
            const color2 = `hsl(${(hue + 60) % 360}, 70%, 50%)`;
            const color3 = `hsl(${(hue + 120) % 360}, 70%, 50%)`;
            const color4 = `hsl(${(hue + 180) % 360}, 70%, 50%)`;
            
            gradientBg.style.background = `linear-gradient(45deg, ${color1}, ${color2}, ${color3}, ${color4})`;
            gradientBg.style.backgroundSize = '400% 400%';
            
            requestAnimationFrame(updateGradient);
        }
        
        updateGradient();
    }
    
    // Neural Network Animation
    function initNeuralNetwork() {
        const gridNodes = document.querySelector('.grid-nodes');
        
        if (gridNodes) {
            // Create animated neural connections
            function createNeuralConnection() {
                const connection = document.createElement('div');
                connection.style.position = 'absolute';
                connection.style.width = '2px';
                connection.style.height = '2px';
                connection.style.background = 'rgba(59, 130, 246, 0.6)';
                connection.style.borderRadius = '50%';
                connection.style.left = Math.random() * 100 + '%';
                connection.style.top = Math.random() * 100 + '%';
                connection.style.animation = 'neural-pulse 3s ease-in-out infinite';
                connection.style.animationDelay = Math.random() * 3 + 's';
                
                gridNodes.appendChild(connection);
                
                // Remove after animation
                setTimeout(() => {
                    connection.remove();
                }, 3000);
            }
            
            // Create connections periodically
            setInterval(createNeuralConnection, 500);
        }
    }
    
    // Typing Effect for Hero Title
    function initTypingEffect() {
        const heroTitle = document.querySelector('hero h1');
        if (heroTitle) {
            const text = heroTitle.textContent;
            heroTitle.textContent = '';
            
            let index = 0;
            function typeText() {
                if (index < text.length) {
                    heroTitle.textContent += text.charAt(index);
                    index++;
                    setTimeout(typeText, 100);
                }
            }
            
            setTimeout(typeText, 1000);
        }
    }
    
    // Initialize all features
    function init() {
        createParticles();
        initMouseGlow();
        initMagneticButtons();
        initCopyAddress();
        initSmoothScrolling();
        initParallax();
        initIntersectionObserver();
        initDynamicGradient();
        initNeuralNetwork();
        initTypingEffect();
    }
    
    // Start the application
    init();
    
    // Add CSS animation for neural pulse
    const style = document.createElement('style');
    style.textContent = `
        @keyframes neural-pulse {
            0% {
                opacity: 0;
                transform: scale(0);
            }
            50% {
                opacity: 1;
                transform: scale(1);
            }
            100% {
                opacity: 0;
                transform: scale(2);
            }
        }
    `;
    document.head.appendChild(style);
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// Add CSS for loading state
const loadingStyle = document.createElement('style');
loadingStyle.textContent = `
    body:not(.loaded) {
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    body.loaded {
        opacity: 1;
    }
`;
document.head.appendChild(loadingStyle);
