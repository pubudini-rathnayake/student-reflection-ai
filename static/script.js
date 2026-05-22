const themeSelect = document.getElementById("themeSelect");

themeSelect.addEventListener("change", function () {
  const selectedTheme = themeSelect.value;

  if (selectedTheme === "kdrama") {
    document.documentElement.style.setProperty("--bg-color", "#ffeef5");
    document.documentElement.style.setProperty("--card-color", "#fff8fb");
    document.documentElement.style.setProperty("--text-color", "#5a4a4a");
    document.documentElement.style.setProperty("--button-color", "#ff7eb3");
  } else if (selectedTheme === "dark") {
    document.documentElement.style.setProperty("--bg-color", "#1e1b18");
    document.documentElement.style.setProperty("--card-color", "#2b2623");
    document.documentElement.style.setProperty("--text-color", "#f5e6cc");
    document.documentElement.style.setProperty("--button-color", "#8b6f47");
  } else if (selectedTheme === "minimal") {
    document.documentElement.style.setProperty("--bg-color", "#ffffff");
    document.documentElement.style.setProperty("--card-color", "#f8f8f8");
    document.documentElement.style.setProperty("--text-color", "#111111");
    document.documentElement.style.setProperty("--button-color", "#333333");
  } else {
    document.documentElement.style.setProperty("--bg-color", "#f5f7fb");
    document.documentElement.style.setProperty("--card-color", "white");
    document.documentElement.style.setProperty("--text-color", "#222");
    document.documentElement.style.setProperty("--button-color", "#7c5cff");
  }
});
