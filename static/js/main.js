const testimonialsData = document.getElementById("testimonials-data");
const testimonials = testimonialsData ? JSON.parse(testimonialsData.textContent) : [];
const testimonialsGrid = document.getElementById("testimonialsGrid");
const prevButton = document.getElementById("prevTestimonial");
const nextButton = document.getElementById("nextTestimonial");
const dotsContainer = document.getElementById("testimonialDots");
const mobileMenuButton = document.querySelector(".mobile-menu-toggle");
const headerMenu = document.getElementById("primaryMenu");

let currentPage = 0;
const testimonialsPerPage = 3;

function closeMobileMenu() {
    if (!mobileMenuButton || !headerMenu) {
        return;
    }

    mobileMenuButton.setAttribute("aria-expanded", "false");
    headerMenu.classList.remove("is-open");
}

function setupMobileMenu() {
    if (!mobileMenuButton || !headerMenu) {
        return;
    }

    // Le bouton inverse simplement l'etat du menu mobile.
    mobileMenuButton.addEventListener("click", function() {
        const isOpen = mobileMenuButton.getAttribute("aria-expanded") === "true";

        mobileMenuButton.setAttribute("aria-expanded", String(!isOpen));
        headerMenu.classList.toggle("is-open", !isOpen);
    });

    // Quand l'utilisateur choisit une section, on referme le menu.
    headerMenu.querySelectorAll("a").forEach(function(link) {
        link.addEventListener("click", closeMobileMenu);
    });

    // Si on agrandit la fenetre vers desktop, le menu revient a son etat ferme.
    window.addEventListener("resize", function() {
        if (window.innerWidth > 1024) {
            closeMobileMenu();
        }
    });
}

function renderDots(pageCount) {
    if (!dotsContainer) {
        return;
    }

    dotsContainer.innerHTML = "";

    if (pageCount <= 1) {
        return;
    }

    for (let index = 0; index < pageCount; index += 1) {
        const dot = document.createElement("span");
        dot.classList.add("dot");

        if (index === currentPage) {
            dot.classList.add("active");
        }

        dotsContainer.appendChild(dot);
    }
}

function displayTestimonials() {
    // Les avis viennent de Django via json_script ; si l'admin est vide, le HTML fallback reste affiche.
    if (!testimonialsGrid || testimonials.length === 0) {
        renderDots(0);
        return;
    }

    testimonialsGrid.innerHTML = "";

    const start = currentPage * testimonialsPerPage;
    const visibleTestimonials = testimonials.slice(start, start + testimonialsPerPage);

    visibleTestimonials.forEach(function(testimonial) {
        const card = document.createElement("article");
        card.classList.add("testimonial-card");

        const quoteIcon = document.createElement("div");
        quoteIcon.classList.add("quote-icon");
        quoteIcon.textContent = "\u201c";

        const text = document.createElement("p");
        text.classList.add("testimonial-text");
        text.textContent = "\u201c" + testimonial.text + "\u201d";

        const author = document.createElement("div");
        author.classList.add("testimonial-author");

        const name = document.createElement("strong");
        name.textContent = testimonial.name;

        const event = document.createElement("span");
        event.textContent = testimonial.event || "";

        author.appendChild(name);
        author.appendChild(event);
        card.appendChild(quoteIcon);
        card.appendChild(text);
        card.appendChild(author);
        testimonialsGrid.appendChild(card);
    });

    renderDots(Math.ceil(testimonials.length / testimonialsPerPage));
}

if (nextButton) {
    nextButton.addEventListener("click", function() {
        const maxPage = Math.ceil(testimonials.length / testimonialsPerPage) - 1;
        currentPage = currentPage < maxPage ? currentPage + 1 : 0;
        displayTestimonials();
    });
}

if (prevButton) {
    prevButton.addEventListener("click", function() {
        const maxPage = Math.ceil(testimonials.length / testimonialsPerPage) - 1;
        currentPage = currentPage > 0 ? currentPage - 1 : maxPage;
        displayTestimonials();
    });
}

displayTestimonials();
setupMobileMenu();
