function Mostrar_Form() {
  // Obtem o valor da categoria selecionada
  const categoria = document.getElementById("categoria").value;

  // Pegar as div com os formularios
  const divPelicula = document.getElementById("pelicula");
  const divCapa = document.getElementById("capa");
  const divCarregador = document.getElementById("carregador");
  const divCabosAdap = document.getElementById("cabos_adaptador");
  const divFone = document.getElementById("fone");
  
  // Atualiza o conteúdo da div com base na seleção
  switch (categoria) {
    case 'pelicula':
      divPelicula.style.display = "block";
      
      divCapa.style.display = "none";
      divCarregador.style.display = "none";
      divCabosAdap.style.display = "none";
      divFone.style.display = "none";
      break;
      
    case 'capa': 
      divCapa.style.display = "block";

      divPelicula.style.display = "none";
      divCarregador.style.display = "none";
      divCabosAdap.style.display = "none";
      divFone.style.display = "none";
      break;
      
    case 'carregador':
      divCarregador.style.display = "block";

      divPelicula.style.display = "none";
      divCapa.style.display = "none";
      divCabosAdap.style.display = "none";
      divFone.style.display = "none";
      break;
      
    case 'cabos_adaptador':
      divCabosAdap.style.display = "block";

      divPelicula.style.display = "none";
      divCapa.style.display = "none";
      divCarregador.style.display = "none";
      divFone.style.display = "none";
      break;
      
    case 'fone':
      divPelicula.style.display = "none";
      divCapa.style.display = "none";
      divCarregador.style.display = "none";
      divCabosAdap.style.display = "none";
      
      divFone.style.display = "block";
      break;
      
    default:
      divPelicula.style.display = "none";
      divCapa.style.display = "none";
      divCarregador.style.display = "none";
      divCabosAdap.style.display = "none";
      divFone.style.display = "none";
      
  }
}
// Adiciona o evento de mudança no select
document.getElementById("categoria").addEventListener("change", Mostrar_Form);