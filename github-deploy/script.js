// Enhanced Neural Pepe Script - Inspired by Top Meme Coins

document.addEventListener('DOMContentLoaded', function() {
    
    // Animated Counter for Holder Count
    function animateCounter() {
        const counter = document.getElementById('holderCount');
        const target = Math.floor(Math.random() * 500) + 100; // Random between 100-600
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            counter.textContent = Math.floor(current);
        }, 16);
    }
    
    // Copy Contract Functionality
    function initCopyContract() {
        const copyBtn = document.getElementById('copyContractBtn');
        const contractAddress = document.getElementById('contractAddress');
        const copiedFeedback = document.getElementById('copiedFeedback');
        
        copyBtn.addEventListener('click', async () => {
            try {
                const address = contractAddress.textContent;
                await navigator.clipboard.writeText(address);
                
                // Show feedback
                copiedFeedback.style.display = 'block';
                copyBtn.style.background = 'var(--gradient-pepe)';
                
                setTimeout(() => {
                    copiedFeedback.style.display = 'none';
                    copyBtn.style.background = 'transparent';
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
    
    // Parallax Effect for Hero Logo
    function initParallax() {
        const heroLogo = document.querySelector('.hero-logo');
        
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            
            if (heroLogo) {
                heroLogo.style.transform = `translateY(${rate}px)`;
            }
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
        const animatedElements = document.querySelectorAll('.about-card, .step-card, .community-card');
        
        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }
    
    // Dynamic Navbar Background
    function initNavbar() {
        const navbar = document.querySelector('.navbar');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 100) {
                navbar.style.background = 'rgba(10, 14, 26, 0.98)';
                navbar.style.backdropFilter = 'blur(20px)';
            } else {
                navbar.style.background = 'rgba(10, 14, 26, 0.95)';
                navbar.style.backdropFilter = 'blur(10px)';
            }
        });
    }
    
    // Hover Effects for Cards
    function initCardEffects() {
        const cards = document.querySelectorAll('.about-card, .step-card, .community-card');
        
        cards.forEach(card => {
            card.addEventListener('mouseenter', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);
            });
        });
    }
    
    // Floating Animation for Memes
    function initFloatingMemes() {
        const memes = document.querySelectorAll('.floating-meme');
        
        memes.forEach((meme, index) => {
            const duration = 15 + (index * 3);
            const delay = index * 2;
            
            meme.style.animationDuration = `${duration}s`;
            meme.style.animationDelay = `${delay}s`;
        });
    }
    
    // Typing Effect for Hero Title
    function initTypingEffect() {
        const title = document.querySelector('.title-gradient');
        if (title) {
            const text = title.textContent;
            title.textContent = '';
            
            let index = 0;
            function typeText() {
                if (index < text.length) {
                    title.textContent += text.charAt(index);
                    index++;
                    setTimeout(typeText, 100);
                }
            }
            
            setTimeout(typeText, 1000);
        }
    }
    
    // Glowing Effect for Crown
    function initCrownGlow() {
        const crown = document.querySelector('.crown-animation');
        
        if (crown) {
            setInterval(() => {
                crown.style.filter = `hue-rotate(${Math.random() * 360}deg)`;
                setTimeout(() => {
                    crown.style.filter = 'none';
                }, 500);
            }, 3000);
        }
    }
    
    // Neural Network Animation
    function initNeuralNetwork() {
        const neuralBg = document.querySelector('.neural-network');
        
        if (neuralBg) {
            // Create neural connections
            function createConnection() {
                const connection = document.createElement('div');
                connection.style.position = 'absolute';
                connection.style.width = '2px';
                connection.style.height = '2px';
                connection.style.background = 'var(--neural-blue)';
                connection.style.borderRadius = '50%';
                connection.style.left = Math.random() * 100 + '%';
                connection.style.top = Math.random() * 100 + '%';
                connection.style.opacity = '0';
                connection.style.animation = 'neuralPulse 3s ease-in-out';
                
                neuralBg.appendChild(connection);
                
                setTimeout(() => {
                    connection.remove();
                }, 3000);
            }
            
            // Create connections periodically
            setInterval(createConnection, 500);
        }
    }
    
    // Button Ripple Effect
    function initRippleEffect() {
        const buttons = document.querySelectorAll('.btn-primary, .btn-secondary');
        
        buttons.forEach(button => {
            button.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.classList.add('ripple');
                
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });
    }
    
    // Add CSS for ripple effect
    const rippleCSS = `
        .btn-primary, .btn-secondary {
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s ease-out;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        
        @keyframes neuralPulse {
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
    
    // Add ripple CSS to head
    const style = document.createElement('style');
    style.textContent = rippleCSS;
    document.head.appendChild(style);
    
    // Initialize all features
    function init() {
        animateCounter();
        initCopyContract();
        initSmoothScrolling();
        initParallax();
        initIntersectionObserver();
        initNavbar();
        initCardEffects();
        initFloatingMemes();
        initTypingEffect();
        initCrownGlow();
        initNeuralNetwork();
        initRippleEffect();
    }
    
    // Start the application
    init();
    
    // Loading animation
    window.addEventListener('load', () => {
        document.body.classList.add('loaded');
    });
    
    // Add loading state CSS
    const loadingCSS = `
        body:not(.loaded) {
            opacity: 0;
            transition: opacity 0.5s ease;
        }
        
        body.loaded {
            opacity: 1;
        }
        
        .hero-logo-container {
            perspective: 1000px;
        }
        
        .hero-logo:hover {
            transform: rotateY(10deg) scale(1.05);
        }
        
        .about-card:hover {
            transform: translateY(-10px) scale(1.02);
        }
        
        .step-card:hover {
            transform: translateY(-5px) scale(1.02);
        }
        
        .community-card:hover {
            transform: translateY(-5px) scale(1.02);
        }
    `;
    
    const loadingStyle = document.createElement('style');
    loadingStyle.textContent = loadingCSS;
    document.head.appendChild(loadingStyle);
});

// Add some additional interactive features
document.addEventListener('DOMContentLoaded', function() {
    
    // Mouse trail effect
    let mouseTrail = [];
    const maxTrailLength = 20;
    
    document.addEventListener('mousemove', (e) => {
        if (mouseTrail.length >= maxTrailLength) {
            const oldTrail = mouseTrail.shift();
            if (oldTrail) oldTrail.remove();
        }
        
        const trail = document.createElement('div');
        trail.className = 'mouse-trail';
        trail.style.left = e.clientX + 'px';
        trail.style.top = e.clientY + 'px';
        trail.style.background = 'var(--neural-blue)';
        trail.style.width = '4px';
        trail.style.height = '4px';
        trail.style.borderRadius = '50%';
        trail.style.position = 'fixed';
        trail.style.pointerEvents = 'none';
        trail.style.opacity = '0.6';
        trail.style.transition = 'opacity 0.5s ease';
        
        document.body.appendChild(trail);
        mouseTrail.push(trail);
        
        setTimeout(() => {
            trail.style.opacity = '0';
        }, 100);
        
        setTimeout(() => {
            trail.remove();
            const index = mouseTrail.indexOf(trail);
            if (index > -1) {
                mouseTrail.splice(index, 1);
            }
        }, 600);
    });
    
    // Add CSS for mouse trail
    const trailCSS = `
        .mouse-trail {
            z-index: 9999;
        }
    `;
    
    const trailStyle = document.createElement('style');
    trailStyle.textContent = trailCSS;
    document.head.appendChild(trailStyle);
});
