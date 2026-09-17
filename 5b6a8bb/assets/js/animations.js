/**
 * Kratam Animation Engine
 * Comprehensive, performant animation system for modern UI
 * Uses IntersectionObserver, requestAnimationFrame, and progressive enhancement.
 * Respects user preferences for reduced motion.
 */
(function() {
    'use strict';

    // State & Config
    let scrollTicking = false;
    let rAF_ID = null;

    // Helper to check if motion is allowed
    const motionOk = () => {
        const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const isPaused = document.body.classList.contains('motion-paused');
        return !prefersReduced && !isPaused;
    };

    // Re-check state if motion preference changes via custom event or matchMedia
    window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', () => {
        document.body.dispatchEvent(new CustomEvent('kratam:motionchange'));
    });

    document.body.addEventListener('kratam:motionchange', () => {
        if (!motionOk()) {
            document.body.classList.add('motion-paused');
        } else {
            document.body.classList.remove('motion-paused');
        }
    });

    /**
     * 1. Advanced Scroll Reveal Engine
     * Assigns specific animation classes and handles staggering
     */
    const initScrollReveal = () => {
        const staggerGroups = [
            { selector: '.specialist-card', class: 'anim-scale-in', stagger: true },
            { selector: '.journey-grid article', class: 'anim-fade-up', stagger: true },
            { selector: '.journal-side > a', class: 'anim-fade-up', stagger: true },
            { selector: '.practice-facts > .container > div', class: 'anim-fade-up', stagger: true }
        ];

        const singleElements = [
            { selector: '.studio-heading', class: 'anim-fade-up' },
            { selector: '.patient-quote', class: 'anim-fade-left' },
            { selector: '.story-video', class: 'anim-fade-right' },
            { selector: '.journal-feature', class: 'anim-scale-in' },
            { selector: '.location-explorer', class: 'anim-fade-up' },
            { selector: '.native-faq', class: 'anim-fade-up' },
            { selector: '.consultation-invitation', class: 'anim-blur-in' },
            { selector: '.surgeon-portrait', class: 'anim-fade-left' },
            { selector: '.surgeon-copy', class: 'anim-fade-right' }
        ];

        // Apply classes and delays
        staggerGroups.forEach(group => {
            const elements = document.querySelectorAll(group.selector);
            elements.forEach((el, index) => {
                el.classList.add(group.class, 'anim-reveal-target');
                el.style.setProperty('--anim-delay', `${index * 120}ms`);
            });
        });

        singleElements.forEach(group => {
            const elements = document.querySelectorAll(group.selector);
            elements.forEach(el => {
                el.classList.add(group.class, 'anim-reveal-target');
            });
        });

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (motionOk()) {
                        entry.target.classList.add('is-animated');
                    } else {
                        // Immediately show if motion is not ok
                        entry.target.style.transition = 'none';
                        entry.target.style.animation = 'none';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'none';
                        entry.target.style.filter = 'none';
                        entry.target.classList.add('is-animated');
                    }
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -60px 0px'
        });

        document.querySelectorAll('.anim-reveal-target').forEach(el => {
            revealObserver.observe(el);
        });
    };

    /**
     * 2. Text Split Animation
     * Splits text into words and chars for staggering
     */
    const initTextSplit = () => {
        // Target specific headings if they exist
        const selectors = [
            '.anim-text-reveal',
            '[data-anim-text]',
            '.studio-hero h1',
            '.studio-hero h2',
            '.consultation-invitation h1',
            '.consultation-invitation h2'
        ];

        const textElements = document.querySelectorAll(selectors.join(', '));
        
        textElements.forEach(el => {
            if (el.dataset.splitted) return; // Prevent double splitting
            
            const text = el.innerText;
            el.innerHTML = '';
            el.dataset.splitted = 'true';
            
            const words = text.split(' ');
            let charIndex = 0;
            
            words.forEach(word => {
                const wordSpan = document.createElement('span');
                wordSpan.className = 'word';
                wordSpan.style.display = 'inline-block';
                wordSpan.style.whiteSpace = 'nowrap';
                
                const chars = word.split('');
                chars.forEach(char => {
                    const charSpan = document.createElement('span');
                    charSpan.className = 'char';
                    charSpan.textContent = char;
                    charSpan.style.display = 'inline-block';
                    charSpan.style.setProperty('--char-index', charIndex++);
                    wordSpan.appendChild(charSpan);
                });
                
                el.appendChild(wordSpan);
                // Add space after word
                const space = document.createTextNode(' ');
                el.appendChild(space);
            });
            
            el.classList.add('anim-reveal-target', 'anim-text-wrapper');
        });
    };

    /**
     * 3. Magnetic Button Effect
     */
    const initMagneticButtons = () => {
        if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

        const buttons = document.querySelectorAll('.anim-btn-magnetic, .btn');
        
        buttons.forEach(btn => {
            btn.addEventListener('pointermove', (e) => {
                if (!motionOk()) return;
                
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                // Max offset ±6px
                const dx = (x / (rect.width / 2)) * 6;
                const dy = (y / (rect.height / 2)) * 6;
                
                btn.style.transform = `translate(${dx}px, ${dy}px)`;
            });
            
            btn.addEventListener('pointerleave', () => {
                btn.style.transform = '';
            });
        });
    };

    /**
     * 4. Card 3D Tilt
     */
    const initCardTilt = () => {
        if (!window.matchMedia('(hover: hover)').matches) return;

        const cards = document.querySelectorAll('.anim-card-tilt, .specialist-card__visual');
        
        cards.forEach(card => {
            card.addEventListener('pointermove', (e) => {
                if (!motionOk()) return;
                
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                // Max rotation ±4deg
                const cx = rect.width / 2;
                const cy = rect.height / 2;
                
                const rotateX = ((y - cy) / cy) * -4;
                const rotateY = ((x - cx) / cx) * 4;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });
            
            card.addEventListener('pointerleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
                setTimeout(() => {
                    card.style.transform = '';
                }, 300); // Wait for transition
            });
        });
    };

    /**
     * 5. Image Parallax on Scroll
     */
    const initImageParallax = () => {
        const parallaxEls = document.querySelectorAll('.anim-img-parallax, .surgeon-portrait img, .discovery-image img, .location-photo img');
        
        const applyParallax = () => {
            if (!motionOk()) {
                parallaxEls.forEach(el => el.style.transform = '');
                return;
            }
            
            const windowHeight = window.innerHeight;
            
            parallaxEls.forEach(el => {
                const rect = el.getBoundingClientRect();
                
                // Only animate if in viewport
                if (rect.top <= windowHeight && rect.bottom >= 0) {
                    // Calculate offset (-1 to 1 based on position in viewport)
                    const centerOffset = (rect.top + rect.height / 2 - windowHeight / 2) / (windowHeight / 2);
                    // Max translate ±30px
                    const translateY = centerOffset * 30;
                    
                    el.style.transform = `translateY(${translateY}px)`;
                }
            });
        };

        const loop = () => {
            if (scrollTicking) {
                applyParallax();
                scrollTicking = false;
            }
            rAF_ID = requestAnimationFrame(loop);
        };
        
        rAF_ID = requestAnimationFrame(loop);
    };

    /**
     * 6. Smooth Section Background Color Transitions
     */
    const initBgTransitions = () => {
        const section = document.querySelector('.consultation-invitation');
        if (!section) return;

        // Create an observer with many thresholds for smooth gradient progress
        const buildThresholdList = () => {
            let thresholds = [];
            let numSteps = 50;
            for (let i = 1.0; i <= numSteps; i++) {
                let ratio = i / numSteps;
                thresholds.push(ratio);
            }
            thresholds.push(0);
            return thresholds;
        };

        const bgObserver = new IntersectionObserver((entries) => {
            if (!motionOk()) return;
            
            entries.forEach(entry => {
                const ratio = entry.intersectionRatio;
                // Transition effect using the ratio (e.g. shift a background position or variable)
                entry.target.style.setProperty('--scroll-progress', ratio);
            });
        }, {
            threshold: buildThresholdList()
        });

        bgObserver.observe(section);
    };

    /**
     * 7. Counter Enhancement
     */
    const initCounterEnhancement = () => {
        // Assume counter logic handles its own counts, we just hook into a completion event or observer
        const counters = document.querySelectorAll('[data-count]');
        
        counters.forEach(counter => {
            const target = counter.getAttribute('data-count');
            
            const observer = new MutationObserver((mutations) => {
                mutations.forEach(mutation => {
                    if (mutation.type === 'characterData' || mutation.type === 'childList') {
                        const val = parseInt(counter.innerText.replace(/\D/g, ''), 10);
                        if (val == target && motionOk()) {
                            // Target reached, apply bounce
                            counter.animate([
                                { transform: 'scale(1)' },
                                { transform: 'scale(1.15)' },
                                { transform: 'scale(1)' }
                            ], {
                                duration: 400,
                                easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)'
                            });
                            observer.disconnect();
                        }
                    }
                });
            });
            
            observer.observe(counter, { childList: true, characterData: true, subtree: true });
        });
    };

    /**
     * 8. Ripple Effect on Buttons
     */
    const initRipples = () => {
        document.addEventListener('click', (e) => {
            const btn = e.target.closest('.btn');
            if (!btn || !motionOk()) return;

            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const ripple = document.createElement('span');
            ripple.className = 'ripple';
            
            // Set styles dynamically if class isn't fully covering it
            ripple.style.position = 'absolute';
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            ripple.style.width = '20px';
            ripple.style.height = '20px';
            ripple.style.background = 'rgba(255,255,255,0.4)';
            ripple.style.borderRadius = '50%';
            ripple.style.transform = 'translate(-50%, -50%) scale(0)';
            ripple.style.pointerEvents = 'none';
            
            // Ensure button handles absolute children
            if (getComputedStyle(btn).position === 'static') {
                btn.style.position = 'relative';
            }
            btn.style.overflow = 'hidden';

            btn.appendChild(ripple);

            ripple.animate([
                { transform: 'translate(-50%, -50%) scale(0)', opacity: 1 },
                { transform: 'translate(-50%, -50%) scale(10)', opacity: 0 }
            ], {
                duration: 600,
                easing: 'ease-out'
            }).onfinish = () => ripple.remove();
        });
    };

    /**
     * 9. Smooth Scroll-Linked Header Shrink Enhancement
     */
    const initHeaderScroll = () => {
        const header = document.querySelector('header');
        if (!header) return;

        const updateHeader = () => {
            if (!motionOk()) {
                header.style.backgroundColor = '';
                header.style.backdropFilter = '';
                return;
            }

            const scrollY = window.scrollY;
            // 0 to 200px range
            let progress = Math.min(scrollY / 200, 1);
            
            // Assuming variable background colors are used, we can interpolate opacity
            header.style.setProperty('--header-scroll-progress', progress);
            
            // Fallback direct styles
            header.style.backgroundColor = `rgba(255, 255, 255, ${progress * 0.9})`; 
            header.style.backdropFilter = `blur(${progress * 10}px)`;
        };

        window.addEventListener('scroll', () => {
            scrollTicking = true;
            updateHeader();
        }, { passive: true });
        
        // Initial call
        updateHeader();
    };

    /**
     * 10. Floating Elements Animation
     */
    const initFloatingElements = () => {
        const floatingEls = document.querySelectorAll('.hero-seal, .small-cross');
        
        floatingEls.forEach((el, index) => {
            if (motionOk()) {
                el.classList.add('anim-float');
                // Vary timing based on index
                el.style.animationDelay = `${index * 0.5}s`;
                el.style.animationDuration = `${3 + (index * 0.2)}s`;
            }
        });
    };

    /**
     * 12. Intersection-based Image Reveal
     */
    const initImageReveal = () => {
        const images = document.querySelectorAll('.discovery-image, .surgeon-portrait, .story-video, .journal-image');
        
        images.forEach(img => {
            img.classList.add('anim-img-reveal', 'anim-reveal-target');
        });
    };

    /**
     * 11. Page Load Orchestration
     */
    const initPageLoad = () => {
        setTimeout(() => {
            document.body.classList.add('anim-page-ready');
            
            // Execute all other inits that might depend on DOM structure
            initTextSplit();
            initImageReveal();
            initScrollReveal();
            initMagneticButtons();
            initCardTilt();
            initImageParallax();
            initBgTransitions();
            initCounterEnhancement();
            initRipples();
            initHeaderScroll();
            initFloatingElements();
            
        }, 100);
    };

    // Main scroll listener to update ticking state for rAF
    window.addEventListener('scroll', () => {
        scrollTicking = true;
    }, { passive: true });

    // Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initPageLoad);
    } else {
        initPageLoad();
    }

})();
