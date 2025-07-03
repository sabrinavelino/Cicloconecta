document.getElementById("cadastroForm").addEventListener("submit", function(e) {
  e.preventDefault();
  document.getElementById("mensagem").textContent = "Cadastro enviado com sucesso!";
  this.reset();
});

// Máscara para CPF ou CNPJ
const cpfcnpjInput = document.getElementById("cpfcnpj");
const tipoInputs = document.getElementsByName("tipo");

function aplicarMascara() {
  const valor = cpfcnpjInput.value.replace(/\D/g, '');
  const tipo = Array.from(tipoInputs).find(r => r.checked).value;

  if (tipo === "fisica") {
    cpfcnpjInput.maxLength = 14;
    cpfcnpjInput.value = valor
      .replace(/^(\d{3})(\d)/, "$1.$2")
      .replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3")
      .replace(/\.(\d{3})(\d)/, ".$1-$2")
      .slice(0, 14);
  } else {
    cpfcnpjInput.maxLength = 18;
    cpfcnpjInput.value = valor
      .replace(/^(\d{2})(\d)/, "$1.$2")
      .replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
      .replace(/\.(\d{3})(\d)/, ".$1/$2")
      .replace(/(\d{4})(\d)/, "$1-$2")
      .slice(0, 18);
  }
}

cpfcnpjInput.addEventListener("input", aplicarMascara);
tipoInputs.forEach(input => input.addEventListener("change", aplicarMascara));