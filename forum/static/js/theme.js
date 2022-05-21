function onThemeChange() {
    var theme = getCookie("theme") == "light" ? "dark" : "light";   
    
    document.getElementById('darkSwitch').checked = theme == "dark";
    registerTheme(theme);

    setInterval(() => {
        window.location.reload(false);
    }, 250);
}

function registerTheme(theme){
    document.cookie = `theme=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    document.cookie = `theme=${theme}; expires=Tue, 19 Jan 2038 03:14:07 UTC; path=/;`;
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}  

function loadTheme(){
    var theme = getCookie("theme");
    if(theme == "") theme = "light";
    document.getElementById('darkSwitch').checked = theme == "dark";
    loadThemeCSS(theme);
}

window.onload = function() {
    loadTheme();
};