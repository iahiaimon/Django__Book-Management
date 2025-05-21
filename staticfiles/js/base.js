

function getHeader() {
    nav = document.querySelector("#header_section")
    nav.innerHTML = `
        <nav class="navbar stiky-top">
            <div class="navbar-barand">
                <a href="${homeUrl}">Home</a>
            </div>
            <div class="navbar-link">
                <a href="${addBookUrl}" >Add Book</a>
            </div>
        </nav>
    `
}

function getFooter() {
    footer = document.querySelector("#footer_section")
    footer.innerHTML = `
        <footer>
            <p>&copy; 2025 All Rights Reserved | By Iahia</p>
        </footer>
    `
}



getHeader()
getFooter()