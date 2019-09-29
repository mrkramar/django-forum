function loadThemeCSS(theme){
    var fileref = document.createElement("link");
    fileref.rel = "stylesheet";
    fileref.type = "text/css";
    fileref.href = "{% static 'css/light-theme.css' %}";

    if(theme == "dark"){
        fileref.href = "{% static 'css/dark-theme.css' %}"
    }else if(theme == "cyber"){
        fileref.href = "{% static 'css/cyber-theme.css' %}"
    }

    document.getElementsByTagName("head")[0].appendChild(fileref);
}

function onThemeChange() {
    var selected = document.getElementById("theme").value
    registerTheme(selected);

    loadThemeCSS(selected);
    window.location.reload(false);
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
    document.getElementById('theme').value=theme;
    loadThemeCSS(theme);
}

window.onload = function() {
    loadTheme();
};