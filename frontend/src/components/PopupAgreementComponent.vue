<template>
    <div id="popupAgreement" class="overlay">
        <div class="popup">
            <h1 class="text-midblue-silentguard text-center font-bold">Consentement</h1>
            <a class="close cursor-pointer">&times;</a>
            <div class="popupContent">
                <p class="mb-2 text-justify">
                  En utilisant Silent Guard, vous acceptez que certaines de vos données soient temporairement collectées le temps d’effectuer la requête. Ces données ne sont en aucun cas conservées une fois le traitement terminé. Lire les conditions générales 
                  <router-link target="_blank" to="/privacy-police" class="font-light text-center underline">ici</router-link>.
                </p>
                <form id="formAgreement">
                    <input id="checkboxAgreement" type="checkbox" required>
                    <label for="checkboxAgreement" class="mb-4">
                        J'ai lu et j'accepte les <router-link target="_blank" to="/privacy-police" class="font-light text-center underline">conditions générales</router-link> de SilentGuard
                    </label>
                    <div class="flex justify-center">
                      <button type="submit" class="cursor-pointer border text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2 my-3">Effectuer la recherche</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<style>
.overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  display: none;
  z-index: 999999;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
}

.popupContent {
  margin: 10px auto;
}
.popup {
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  border-radius: 5px;
  width: 50%;
  position: relative;
  transition: all 5s ease-in-out;
}
.popup h1 {
  margin-top: 0;
  padding: 10px 0;
}
.popup .close {
  position: absolute;
  top: 20px;
  right: 30px;
  transition: all 200ms;
  font-size: 30px;
  font-weight: bold;
  text-decoration: none;
  color: #333;
}
.popup .close:hover {
  color: rgba(51,110,128,1);
}
.popup .content {
  max-height: 30%;
  overflow: auto;
}

@media screen and (max-width: 700px){
  .popup{
    width: 70%;
  }
}

@keyframes rotation {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
} 
</style>