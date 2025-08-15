function openTab(event, tabName) {
    document.querySelectorAll(".tabcontent")
        .forEach(element => element.classList.remove("is-active"))
    
    document.querySelectorAll(".tablinks")
        .forEach(button => button.classList.remove("active"))
    
    document.getElementById(tabName)?.classList.add("is-active")
    event.currentTarget.classList.add("active")
}