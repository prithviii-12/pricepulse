function searchProduct() {
    let product = document.getElementById("product").value;

    fetch(`/search?product=${product}`)
        .then(res => res.json())
        .then(data => {

            let resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "";

            if (data.length === 0) {
                resultsDiv.innerHTML = "<p>No products found</p>";
                return;
            }

            data.forEach((item, index) => {
                let highlight = index === 0 ? "🏆 Best Deal" : "";

                resultsDiv.innerHTML += `
                    <div class="result-card">
                        <h3>${item.title}</h3>
                        <p><b>${item.site}</b></p>
                        <p>₹ ${item.price}</p>
                        <p style="color: green;">${highlight}</p>
                        <img src="${item.link}" width="120">
                    </div>
                `;
            });
        });
}