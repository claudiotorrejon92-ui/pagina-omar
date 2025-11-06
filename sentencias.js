window.addEventListener("DOMContentLoaded", () => {
  const cont = document.getElementById("lista-sentencias");
  const sentencias = JSON.parse(localStorage.getItem("sentencias")) || [];
  cont.innerHTML = sentencias.reverse().map(s =>
    `<article class="sentencia">
      <h3>${s.titulo}</h3>
      <p class="fecha">${s.fecha}</p>
      <p>${s.descripcion}</p>
      ${s.url ? `<a href="${s.url}" target="_blank" class="btn">Ver fallo completo</a>` : ""}
    </article>`
  ).join("");
});
