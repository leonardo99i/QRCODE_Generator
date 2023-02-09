/* The above code is creating a QR code from the text input. */
const generateButton = document.getElementById("generate-button");
const textInput = document.getElementById("text");

/* Creating a QR code from the text input. */
generateButton.addEventListener("click", function() {
  const text = textInput.value;
  const qrCode = new QRCode(document.getElementById("qr-code"), {
    text: text,
    width: 128,
    height: 128,
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
  });

/* Creating a download button. */
  const downloadButton = document.createElement("a");
  downloadButton.innerHTML = "Baixar QR code";
  downloadButton.href = qrCode.toDataURL();
  downloadButton.download = "qr-code.png";
  downloadButton.style.marginTop = "20px";
  document.body.appendChild(downloadButton);
});
