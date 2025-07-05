document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault();

  const usuario = document.getElementById("usuario").value.trim();
  const senha = document.getElementById("senha").value.trim();
  const msg = document.getElementById("mensagem");

  if (usuario === "" || senha === "") {
    msg.textContent = "Preencha todos os campos.";
    return;
  }

  // Exemplo simples de validação 
  if (usuario === "admin" && senha === "1234") {
    msg.style.color = "green";
    msg.textContent = "Login bem-sucedido!";
    // redirecionar após 1 segundo
    setTimeout(() => {
      window.location.href = "main.html";
    }, 1000);
  } else {
    msg.style.color = "red";
    msg.textContent = "Usuário ou senha incorretos.";
  }
});