function toggleNav() {
            const sidebar = document.getElementById("mySidebar");
            const wrapper = document.getElementById("wrapper");
            sidebar.classList.toggle("collapsed");
            wrapper.classList.toggle("collapsed");
        }