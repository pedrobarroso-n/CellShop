/**
 * @author: Gleison Pereira
 */
document.getElementById("categoria").addEventListener("change", Mostrar_Form);
document.getElementById("ProdutoPelicula").addEventListener("change", MostrarDadosPelicula);
document.getElementById("ProdutoCapa").addEventListener("change", MostrarDadosCapa);
document.getElementById("ProdutoCarregador").addEventListener("change", MostrarDadosCarregador);
document.getElementById("ProdutoCabos_adaptador").addEventListener("change", MostrarDadosCabos_adaptador);
document.getElementById("ProdutoFone").addEventListener("change", MostrarDadosFone);



//Pelicula
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

function MostrarDadosPelicula() {
  // Obtém o valor selecionado no dropdown
  let Dados = document.getElementById("ProdutoPelicula").value.replace("(", ' ').replace(")",' ');
  let Json = {Dados: Dados}

  // Seleciona o elemento onde os dados serão atualizados
  let atualizarDados = document.getElementById("MostrarInfoPelicula");

  switch (Dados){
    case "#":
      atualizarDados.style.display= "none";
      break;

    default:
      atualizarDados.style.display= "block";
      break;
  }

  let Info = document.getElementsByName("dados")[0];

  Info.value = Dados;
}


/**
 * Capa
 */
function MostrarDadosCapa() {
  // Obtém o valor selecionado no dropdown
  let Dados = document.getElementById("ProdutoCapa").value.replace("(", ' ').replace(")",' ');
  let Json = {Dados: Dados}

  // Seleciona o elemento onde os dados serão atualizados
  let atualizarDados = document.getElementById("MostrarInfoCapa");

  switch (Dados){
    case "#":
      atualizarDados.style.display= "none";
      break;

    default:
      atualizarDados.style.display= "block";
      break;
  }

  let Info = document.getElementsByName("dados")[0];

  Info.value = Dados;
}

//Carregador

function MostrarDadosCarregador() {
  // Obtém o valor selecionado no dropdown
  let Dados = document.getElementById("ProdutoCarregador").value.replace("(", ' ').replace(")",' ');
  let Json = {Dados: Dados}

  // Seleciona o elemento onde os dados serão atualizados
  let atualizarDados = document.getElementById("MostrarInfoCarregador");

  switch (Dados){
    case "#":
      atualizarDados.style.display= "none";
      break;

    default:
      atualizarDados.style.display= "block";
      break;
  }

  let Info = document.getElementsByName("dados")[0];

  Info.value = Dados;
}

//Cabos_adaptador

function MostrarDadosCabos_adaptador() {
  // Obtém o valor selecionado no dropdown
  let Dados = document.getElementById("ProdutoCabos_adaptador").value.replace("(", ' ').replace(")",' ');
  let Json = {Dados: Dados}

  // Seleciona o elemento onde os dados serão atualizados
  let atualizarDados = document.getElementById("MostrarInfoCabos_adaptador");

  switch (Dados){
    case "#":
      atualizarDados.style.display= "none";
      break;

    default:
      atualizarDados.style.display= "block";
      break;
  }

  let Info = document.getElementsByName("dados")[0];

  Info.value = Dados;
}

//Fone
function MostrarDadosFone() {
  // Obtém o valor selecionado no dropdown
  let Dados = document.getElementById("ProdutoFone").value.replace("(", ' ').replace(")",' ');
  let Json = {Dados: Dados}

  // Seleciona o elemento onde os dados serão atualizados
  let atualizarDados = document.getElementById("MostrarInfoFone");

  switch (Dados){
    case "#":
      atualizarDados.style.display= "none";
      break;

    default:
      atualizarDados.style.display= "block";
      break;
  }

  let Info = document.getElementsByName("dados")[0];

  Info.value = Dados;
}