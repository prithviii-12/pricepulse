function searchProduct() {
    let product = document.getElementById("product").value;

    fetch(`/search?product=${product}`)
        .then(res => res.json())
        .then(data => {

            let resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "";

            data.forEach((item, index) => {
                let badge = index === 0 ? "🔥 Best Price" : "";

                resultsDiv.innerHTML += `
                    <div class="card">
                        <img src="${item.image}">
                        <h3>${item.title}</h3>
                        <p>${item.site}</p>
                        <p class="price">₹ ${item.price}</p>
                        <p class="best">${badge}</p>
                        <a href="${item.link}" target="_blank">View</a>
                    </div>
                `;
            });
        });
}
