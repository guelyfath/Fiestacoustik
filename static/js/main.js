const testimonials = [
    {
        text: "Une ambiance parfaite du début à la fin, nos invités ont adoré !",
        name: "Marie & Julien",
        event: "Mariage"
    },
    {
        text: "Fiestacoustik a mis une super ambiance pour notre fête communale. Professionnel et à l’écoute !",
        name: "Comité des fêtes",
        event: "Saint-Aubin"
    },
    {
        text: "Musicien talentueux, répertoire au top et très bonne communication. On recommande à 100% !",
        name: "Thomas",
        event: "Soirée privée"
    },
    {
        text: "Une prestation chaleureuse, très bien adaptée à notre public.",
        name: "Restaurant Le Patio",
        event: "Soirée restaurant"
    },
    {
        text: "Très belle présence, bon contact et ambiance parfaite pour notre événement.",
        name: "Claire",
        event: "Anniversaire"
    },
    {
        text: "Un vrai moment musical, simple, vivant et professionnel.",
        name: "Association locale",
        event: "Événement public"
    }
];

const testimonialsGrid = document.getElementById("testimonialsGrid");
const prevButton = document.getElementById("prevTestimonial");
const nextButton = document.getElementById("nextTestimonial");
const dots = document.querySelectorAll(".dot");

let currentPage = 0;
const testimonialsPerPage = 3;

function displayTestimonials() {
    testimonialsGrid.innerHTML = "";

    const start = currentPage * testimonialsPerPage;
    const end = start + testimonialsPerPage;

    const visibleTestimonials = testimonials.slice(start, end);

    visibleTestimonials.forEach(function(testimonial) {
        const card = document.createElement("article");
        card.classList.add("testimonial-card");

        card.innerHTML = `
            <div class="quote-icon">“</div>

            <p class="testimonial-text">
                “${testimonial.text}”
            </p>

            <div class="testimonial-author">
                <strong>${testimonial.name}</strong>
                <span>${testimonial.event}</span>
            </div>
        `;

        testimonialsGrid.appendChild(card);
    });

    updateDots();
}

function updateDots() {
    dots.forEach(function(dot, index) {
        if (index === currentPage) {
            dot.classList.add("active");
        } else {
            dot.classList.remove("active");
        }
    });
}

nextButton.addEventListener("click", function() {
    const maxPage = Math.ceil(testimonials.length / testimonialsPerPage) - 1;

    if (currentPage < maxPage) {
        currentPage++;
    } else {
        currentPage = 0;
    }

    displayTestimonials();
});

prevButton.addEventListener("click", function() {
    const maxPage = Math.ceil(testimonials.length / testimonialsPerPage) - 1;

    if (currentPage > 0) {
        currentPage--;
    } else {
        currentPage = maxPage;
    }

    displayTestimonials();
});

displayTestimonials();