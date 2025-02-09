<template>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Le guide de base de la protection de la vie privée pour les particuliers par SilentGuard
        </h1>
        <div class="flex justify-center gap-4 mb-4">
            <a href="/doc_individuals.pdf" download class="cursor-pointer border text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2">Télécharger</a>
        </div>
        <div class="flex justify-center gap-4 flex-wrap">
            <span>Vous êtes une organisation ?</span>
            <router-link to="/doc-organisations" class="text-lightblue-silentguard text-center underline">
                ⇒ Conseils pour les organisations
            </router-link>
        </div>
    </div>
    <div class="container mx-auto py-4 px-6 pb-20 text-justify">
        <p class="mb-4">
            Nous allons voir ici de manière simple et intuitive comment nous allons pouvoir renforcer votre sécurité en ligne. Dans ce livret nous allons donc aborder des conseils directement liés à la cyber sécurité en générale et ensuite à la préservation de votre vie privée numérique. Bonne lecture !             En 2021, le cybercrime a coûté 6 000 milliards de dollars américains, un coût qui va passer à 10 500 milliards de dollars vers 2025, avec un risque d’être attaqué qui augmente de plus en plus également. La mise en place d’un système de cybersécurité solide est donc vitale.
        </p>
        <p class="mb-4">
            Avant d’aller plus loin. Nous allons parler de divers produits, solutions ou marques. Nous ne sommes affiliés à aucune compagnie et nous faisons nos recommendations via des tests, ainsi que des retours utilisateurs et professionnels. 
        </p>

        <h1 class="text-midblue-silentguard text-center my-8 font-bold">1. La cybersécurité et ses outils</h1>
        <p class="mb-4">
            Notre but ici est de parler de la protection des données. Avoir une bonne sécurité générale sur internet va être un avantage crucial. Les cyberattaques sont de plus en plus présentes. Selon le <a href="https://www.cybermalveillance.gouv.fr/" target="_blank" class="underline text-midblue-silentguard">GIP ACYMA</a> (Groupement d’Intérêt Public Action contre la Cyber Malveillance) il y a eu plus de 173 000 demandes d’assistance en 2021, une hausse de 65% comparé à 2021. Nous allons donc voir comment se prémunir de ces attaques. Notamment des 3 plus utilisés. 
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">a. Houston y a-t-il un problème ? (les données qui ont déjà “fuité”)</h2>
        <p class="mb-4">
            Sans le savoir certaines de vos informations ont peut-être déjà “leaké” (la base de données d’une entreprise qui possédait vos données s’est fait piraté et volé ces données) pour le savoir rendez-vous sur le site <a href="https://haveibeenpwned.com/" target="_blank" class="underline text-midblue-silentguard">I been pawnd ?</a> et entrer votre mail sur la page principale. Si le résultat est vert tout va bien ! 
        </p>
        <p class="mb-4">
            Si en revanche le résultat est négatif, il faut alors directement prendre les mesures nécessaires en fonction des informations qui ont fuité, le mieux reste de mettre à jour les informations de connexions de la plateforme ciblée, et de vérifier les autres données (comme l’adresse mail !). 
        </p>
        <img :src="`/individuals-1.png`" class="md:w-1/3 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Ces informations vous permettent également d’être plus vigilant. Les trois attaques les plus utilisées en 2024 sont les suivantes : 
        </p>
        <img :src="`/individuals-2.png`" class="md:w-1/3 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Plus de 60% des attaques sont soit des attaques de hameçonnage (phishing) dans 38% des cas, du piratage de compte dans 17.1% des cas et pour finir 9.6% des gens sont victimes d’un faux support technique. 
        </p>
        <p class="mb-4">
            La bonne nouvelle est que vous pouvez contrer vous même ces trois attaques !! Elles vont toutes nécessiter vos informations privées comme votre mail et votre numéro de téléphone. D’où l’importance de protéger vos données. Mais si vos données sont déjà en vente sur le darknet il vous suffira d’être vigilant sur les mails et les appels que vous allez recevoir avec ces quelques conseils simples : 
        </p>
        <ul class="list-disc pl-5 mb-4">
            <li>Aucun conseiller ou administrateur d’aucun service n’a besoin de votre mots de passe.</li>
            <li>Si vous n’avez pas confiance en un lien que l’on vous a envoyé par mail, passez par une recherche internet plutôt que par ce lien.</li>
            <li>Si on vous met la pression pour agir immédiatement c’est le moment de prendre du recul et de bien réfléchir à la situation.</li>
            <li>Aucun conseiller ou administrateur d’aucun service n’a besoin de votre mots de passe.</li>
            <li>Si vous devez payer sur un site auxquelles vous n’avez pas confiance passez par un service tier comme <a href="https://www.paypal.com/fr/home" class="underline text-midblue-silentguard" target="_blank">Paypal</a> ou bien crée <a href="https://www.journaldunet.fr/patrimoine/guide-des-finances-personnelles/1502381-carte-bancaire-virtuelle-definition-et-utilisation/" class="underline text-midblue-silentguard" target="_blank">une carte virtuelle</a> via votre banque.</li>
        </ul>
        <p class="mb-4">
            Si vous avez été victimes d’une attaque contactez sans tarder <a href="https://www.cybermalveillance.gouv.fr" class="underline text-midblue-silentguard" target="_blank">l’Assistance et prévention du risque numérique</a>. 
        </p>
        <p class="mb-4">
            Il reste à voir comment se protéger contre les piratages de compte. Cela se passe dans la prochaine section !
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">b. La redondance, il y a pas mieux ! (activation de la double authentification)</h2>
        <p class="mb-4">
            La double authentification est un moyen très sûr de renforcer la sécurité de ses comptes les plus critiques. Nous vous recommandons donc de l’activer sur les sites qui possèdent vos informations bancaires permanentes (Amazon, Fnac, …), les sites qui pourraient permettre d’usurper votre identité (sites gouvernementaux) et surtout l’accès à votre banque et à votre adresse mail.
        </p>
        <p class="mb-4">
            Sécuriser son adresse mail est très important car sur quasiment tous les sites on peut utiliser l’option “mot de passe oublié”. Alors il suffit à l’attaquant d’avoir votre compte mail pour accéder à tous vos autres comptes. 
        </p>
        <p class="mb-4">
            La double authentification va faire que, lorsque vous vous connectez depuis un nouvel appareil, on va vous demander en plus de votre mots de passe classique un mots de passe actualisé toutes les 30 secondes sur un autre appareil (généralement votre téléphone) sera demander. Cette protection découragera la majeure partie des attaquants de continuer l’attaque !
        </p>
        <p class="mb-4">
            Pour l’activer, allez dans les paramètres de votre compte et dans l’onglet sécurité. Vous y trouverez alors un paramètre lié à la double authentification (ou la validation en deux étapes).
        </p>
        <p class="mb-4">
            Comme application de double authentification, vous pouvez utiliser <a href="https://2fas.com" target="_blank" class="underline text-midblue-silentguard">2Fas</a> qui a l’avantage d’être <a href="https://fr.wikipedia.org/wiki/Open_source" target="_blank" class="underline text-midblue-silentguard">open source</a> et donc plus transparent sur son fonctionnement. Ils ont d’ailleurs plusieurs <a href="https://2fas.com/how-to-enable-2fa/">tutoriels vidéos</a> pour vous aider à activer la double authentification. 
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">c. Comment créer un mots de passe fort et s’en souvenir ?</h2>
        <p class="mb-4">
            Pour renforcer l’accès à nos comptes il vaut mieux utiliser un mots de passe fort. Je pense que tout le monde à déjà vue ce genre de schéma mais je me permets de mettre ici une version traduite du document de la compagnie <a href="https://www.hivesystems.com/blog/are-your-passwords-in-the-green" target="_blank" class="underline text-midblue-silentguard">Hives Systems</a> sur le temps que mettent chaque type de mots de passe à être trouvé par un attaquant : 
        </p>
        <img :src="`/individuals-3.png`" class="md:w-1/3 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Nous voyons donc que la complexité et la longueur du mots de passe a un impact important sur le temps mis à le déchiffrer. Les recommandations de l’ANSSI actuelles sont d’avoir un mots de passe d’au minimum 12 caractères avec nombres, lettres majuscules, lettres minuscules et symboles. 
        </p>
        <p class="mb-4">
            Mais comment créer ce genre de mots de passe complexe lorsque l'on manque d'imagination ? Bien sûr il faut bien éviter de s’inspirer de nos données personnelles.
        </p>
        <p class="mb-4">
            C’est là qu'interviennent les gestionnaires de mots de passe. Ces coffre-forts numériques vont générer des mots de passe très complexes tels que celui-ci via le gestionnaire de mots de passe Proton Pass :
        </p>
        <img :src="`/individuals-4.png`" class="md:w-1/3 sm:w-100 mx-auto" />
        <div class="italic text-center mb-4">mots de passe utilisé à titre d’exemple (n’est utilisé nul part)</div>
        <p class="mb-4">
            Maintenant vient la question de comment mémoriser ce type de mots de passe ? Eh bien pas besoin ! Le gestionnaire de mots de passe va les retenir et vous les donner quand vous en aurez besoin. Par exemple, si je veux me connecter à myEfrei la plateforme de l’école, mon gestionnaire de mots de passe va me proposer mon identifiant et mon mots de passe.
        </p>
        <img :src="`/individuals-5.png`" class="md:w-1/4 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Le gestionnaire sera protégé par un mots de passe fort que vous seul connaîtrez et qui, pour des raisons de sécurité, ne peut être régénéré si vous l’oubliez, il faut donc s’en souvenir à coup sûr ! 
        </p>
        <p class="mb-4">
            Pour choisir votre mots de passe nous vous conseillons d'abord ne pas prendre de gestionnaire multi-device gratuit. En effet si le gestionnaire actualise votre banque de mots de passe gratuitement, il doit trouver un moyen de se financer. Ce sera sûrement par le biais de vente  de données ! Choisissez donc un gestionnaire que vous financez pour vous assurer une bonne protection comme <a href="https://bitwarden.com/fr-fr/" target="_blank" class="underline text-midblue-silentguard">BitWarden</a>, <a href="https://1password.com/fr" target="_blank" class="underline text-midblue-silentguard">1password</a> ou <a href="https://proton.me/fr/pass" target="_blank" class="underline text-midblue-silentguard">ProtonPass</a>. La version gratuite de ces gestionnaires est certe très limitée mais elle permet de vous faire une idée du service ! Si vous ne voulez pas débourser d'argent, il existe également des solutions hors ligne gratuite comme <a href="https://keepass.info" target="_blank" class="underline text-midblue-silentguard">keepass</a>. En revanche, tous vos mots de passe ne seront accessibles que sur la machine qui les stocke.
        </p>
        <p class="mb-4">
            Enfin nous allons vous donner un dernier conseil pour créer vous même un mots de passe fort. Créez des phrases ! Une phrase impersonnelle peut faire un mots de passe très efficace tout en restant difficile à trouver pour un ordinateur qui n’utilise pas la logique humaine. Par exemple “<b>JeVaisALaPecheLe8Janvier</b>” est un mots de passe fort qui respecte toutes les normes de l’ANSSI et est assez facile à retenir.
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">d. Les extensions à utiliser</h2>
        <p class="mb-4">
            Maintenant que vous avez les bons réflexes de sécurité, nous allons vous proposer quelques extensions. Ces extensions sont comme des améliorations que l’on fixe sur notre navigateur. Ici les extensions recommandées sont sur le navigateur Firefox mais il en existe d'autres similaires sur les autres navigateurs.
        </p> 
        <p class="mb-4"><u>L'extension de votre gestionnaire de mots de passe</u></p>
        <p class="mb-4">
            Comme vu précédemment, un gestionnaire de mots de passe est un très bon allié. L’avoir d'intégré à votre navigateur vous facilitera la vie. Tous les gestionnaires cités possèdent leur propre extension. Pour ne pas vous faire avoir, vérifiez bien les notes données à l'extension et voyez par vous-même si elle est recommandée par le navigateur lui-même.
        </p>
        <img :src="`/individuals-6.png`" class="md:w-2/3 sm:v-100 mx-auto mb-4" />
        <p class="mb-4"><u>Extensions contre les sites malveillants et leurs scripts</u></p>
        <p class="mb-4">
            Tous les sites web fonctionnent avec des scripts. Si ces morceaux de codes sont inoffensifs la plupart du temps ils peuvent s’avérer dangereux si vous vous rendez sur des sites malveillants. <a href="https://addons.mozilla.org/fr/firefox/addon/noscript/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=collection" target="_blank" class="underline text-midblue-silentguard">NoScript Security Suite</a> vous protègera des scripts qui n'agissent pas de manière normale.
        </p>
        <p class="mb-4">
            Vous voila maintenant bien préparé pour affronter la jungle numérique. Mais n’oubliez jamais ce conseil : malgré une excellente protection, le plus important est de rester vigiliant car la plupart des attaques aboutissent à cause d’une erreur humaine. Et si vous êtes attentif, aucun hacker ne pourra vous atteindre facilement !
        </p>

        <h1 class="text-midblue-silentguard text-center my-8 font-bold">2. La protection de sa vie privée</h1>
        <p class="mb-4">
            Comment protéger sa vie privée dans le plus grand espace de communication jamais créé par l’homme ? Vaste sujet ! Nous allons commencer simplement par vous dire qu’il n’est pas vraiment possible de complètement “disparaître d’internet”. Même si vous n’y avez jamais mis les pieds, vous avez des traces sur le net. Mais ce que nous allons faire ici, c’est vous montrer comment, par des gestes simples, limiter au maximum votre <a href="https://www.malwarebytes.com/fr/cybersecurity/basics/digital-footprint" target="_blank" class="underline text-midblue-silentguard">empreinte numérique</a>. Pour qu’une personne lambda, un attaquant ou une entreprise en sache le moins possible. 
        </p>


        <h2 class="text-midblue-silentguard my-4 font-bold">a. Comment faire disparaître nos données en ligne ?</h2>
        <p class="mb-4">
            Comme nous l’avons dit, nous générons des données lorsque nous sommes en ligne, et les data brokers (les entreprises qui conservent nos données) les gardent comme ressource à utiliser. Il existe une manière de forcer ces géants à supprimer vos données : la voie légale ! Si vous en faites la demande, un data broker est normalement obligé de supprimer vos informations.
        </p>
        <p class="mb-4">
            <a href="https://duckduckgo.com" target="_blank" class="underline text-midblue-silentguard">PrivacyRight</a> possède une liste des emails des data brokers à contacter. Mais que mettre dans le mail ? La CNIL propose des modèles d’emails pré-rédigés pour vous aider. <a href="https://www.cnil.fr/fr/modele/courrier/supprimer-des-donnees-personnelles" target="_blank" class="underline text-midblue-silentguard">Voici celui destiné à la suppression des données</a>.
        </p>
        <p class="mb-4">
            Attention toutefois, en fonction de la localisation et de la politique de l’entreprise, il peut être compliqué de forcer la suppression, mais c’est toujours une tentative à envisager. 
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">b. Comment protéger ses comptes en ligne ?</h2>
        <p class="mb-4">
            Nous pouvons, sans le vouloir, laisser des informations visibles sur internet, alors que quelques actions simples peuvent nous protéger. Prenons l’exemple de Strava, un "réseau social pour sportifs" : 
        </p>
        <p class="mb-4">
            Par défaut, un compte Strava est public. Tout le monde peut voir toutes les activités du compte dans les moindres détails.
        </p>
        <p class="mb-4">
            Pour limiter cela, il faut, comme pour toutes les applications, aller dans les paramètres, puis dans l’onglet confidentialité.
        </p>
        <img :src="`/individuals-12.png`" class="md:w-1/2 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            On peut voir ici une page avec une bonne confidentialité, puisque seules les personnes dont on a accepté l’abonnement peuvent voir nos activités. Ce type de paramètre existe sur la plupart des réseaux sociaux et doit être activé pour renforcer votre vie privée, tout en continuant à profiter de ces plateformes ! 
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">c. Quels navigateur et moteur de recherche pour surfer sur le net ?</h2>
        <p class="mb-4">
            Commençons par l’interface qui vous permet d’accéder au web. Ici il faut bien différencier le navigateur et le moteur de recherche. Le navigateur c’est l’application qui va être installée sur votre ordinateur, le support. Votre navigateur actuel est probablement Chrome comme 60% des français. 
        </p>
        <p class="mb-4">
            Et ensuite dans ce navigateur il y a le moteur de recherche, la fenêtre dans laquelle vous allez poser votre question. Et là vous utilisez très probablement Google qui est le choix de 87% des français. 
        </p>
        <p class="mb-4">
            Mais au final, quoi utiliser ? Et quelle est la différence ? 
        </p>
        <p class="mb-4">
            <a href="https://privacytests.org" target="_blank" class="underline text-midblue-silentguard">PrivacyTest.org</a> regroupe un benchmark de plusieurs navigateurs. En le parcourant on remarque que plusieurs navigateur se démarquent : 
        </p>
        <ul class="list-disc pl-5 mb-4">
            <li>Brave</li>
            <li>Firefox</li>
            <li>LibreFox</li>
            <li>DuckDuckGo</li>
        </ul>
        <p class="mb-4">
            Ces quatre navigateurs offrent une bonne protection. Cependant, LibreFox et DuckDuckGo étant des navigateurs peu utilisés, ils sont moins éprouvés et disposent de moins de fonctionnalités. Le choix sera donc plus à faire entre Brave et Firefox. 
        </p>
        <p class="mb-4">
            Et pour résumer, entre nos deux navigateurs, <a href="https://brave.com/fr/download/" target="_blank" class="underline text-midblue-silentguard">Brave</a> sera légèrement plus rapide là où FireFox sera plus gourmand en ressources. Cependant Firefox garde l’avantage d’être un organisme à but non lucratif mais fait beaucoup avec la Mozilla fondation pour promouvoir la vie privée en ligne. 
        </p>
        <div class="flex mx-auto w-100 justify-center gap-2 mb-4 flex-wrap">
            <img :src="`/individuals-7.png`" class="md:w-1/4 sm:w-100" />
            <img :src="`/individuals-8.png`" class="md:w-1/4 sm:w-100" />
        </div>
        <p class="mb-4">
            Donc pour résumer, si vous voulez un navigateur sûr et le plus rapide, optez pour Brave. Si vous voulez un navigateur également très sûr qui va militer pour le plus grand nombre pour la vie privée de manière libre et indépendante, soutenez <a href="https://www.mozilla.org/fr/firefox/new/" target="_blank" class="underline text-midblue-silentguard">Firefox</a> ! 
        </p>
        <p class="mb-4">
            Pour ce qui va être du moteur de recherche il n’y a qu’un moteur de recherche connu qui va se concentrer sur la protection de la vie privée : <a href="https://duckduckgo.com" target="_blank" class="underline text-midblue-silentguard">DuckDuckGo</a>. 
        </p>

        <h2 class="text-midblue-silentguard my-4 font-bold">d. LE VPN, l’arme ultime ?</h2>
        <p class="mb-4">
            Si vous êtes sur internet vous avez forcément entendu parler des VPN non ? Depuis 5 ans on les voit partout via des pubs qui nous promettent de bêtes réductions en se localisant partout dans le monde. Mais un VPN ce n'est pas du tout fait pour ça !
        </p>
        <p class="mb-4">
            Les VPN (Virtual Private Network) vont créer un tunnel sécurisé entre votre machine et le site web que vous allez consulter. L’avantage principal se situe au niveau de la vie privée ! Toutes les personnes qui cherchent à récupérer vos informations personnelles à votre insu échoueront face au VPN. Vous êtes donc protégé des attaques de type "<a href="https://fr.wikipedia.org/wiki/Attaque_de_l'homme_du_milieu" target="_blank" class="underline text-midblue-silentguard">homme du milieu</a>" (Man-in-the-Middle).
        </p>
        <img :src="`/individuals-9.png`" class="md:w-1/3 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Attention tout de même, un VPN ne vous protège pas de tout et tout le monde, votre Fournisseur d’accès à internet (FAI) aura toujours des informations sur vous et votre activité en ligne. Ainsi que le site web que vous allez consulter. 
        </p>
        <p class="mb-4">
            Donc oui, un VPN va vous protéger de nombreuses attaques en ligne, oui il va protéger votre vie privée et oui vous allez sûrement pouvoir faire des économies en prenant un abonnement quelconque en Argentine (ce qui est une utilisation discutable que nous ne vous recommandons pas). Un VPN va également vous servir à esquiver le censure dans votre pays. Même en France certains contenus en ligne sont bloqué pour des raisons politiques donc un VPn est un bon ajout à votre arsenal numérique, MAIS : 
        </p>
        <ul class="list-disc pl-5 mb-4">
            <li>Il ne vous rend pas invincible, restez responsable en ligne et faites attention à tout ce que vous faites, la principale faille restera toujours présente puisqu’il s’agit de nous même !</li>
            <li>Comme pour des solutions vus précédemment n'utilisez jamais de VPN gratuit ! Pour générer de l’argent il vendra vos données voire pire. Privilégiez une solution payante de qualité. Dans notre équipe nous utilisons uniquement le VPN de la firme suisse Proton qui nous donne entière satisfaction. Mais nous vous invitons à regarder d'autres offres qui pourraient être tout aussi intéressantes tout en restant vigilant. </li>
        </ul>

        <h2 class="text-midblue-silentguard my-4 font-bold">e. La zone grise des bloqueurs de pubs</h2>
        <p class="mb-4">
            Les bloqueurs de publicité (ou AdBlocker) sont assez connus du grand public mais seulement <a href="https://backlinko.com/ad-blockers-users" target="_blank" class="underline text-midblue-silentguard">31% des français</a> l’utilisent. Et certaines personnes ne l'utilisent pas car elles ne savent pas si ce genre de dispositif est légal ou non. Les bloqueurs de publicité sont certes controversés mais l’année dernière un <a href="https://goodtech.info/une-liberte-retrouvee-avec-les-adblocks-actives/" target="_blank" class="underline text-midblue-silentguard">tribunal allemand a légitimé l’utilisation d’un bloqueur de publicité</a>. Cela crée donc une jurisprudence au niveau européen. Ne vous privez donc pas d’utiliser un bloqueur de publicité pour limiter les données générées par celle-ci et avoir une page web plus agréable !
        </p>
        <img :src="`/individuals-10.png`" class="md:w-1/4 sm:w-100 mx-auto mb-4" />

        <h2 class="text-midblue-silentguard my-4 font-bold">f. Les extensions à utiliser</h2>
        <p class="mb-4">
            Nous allons ici parler de quelques <b>extensions</b> qui vont faciliter la protection de votre vie privée en ligne.
        </p>
        <p class="mb-4">
            Premièrement comme dit dans la dernière section <b>un bloqueur de publicité est intéressant et légal à installer et à utiliser</b>. Nous vous conseillons <a href="https://ublockorigin.com/fr" target="_blank" class="underline text-midblue-silentguard">uBlockOrigin</a> une solution fiable et <b>open source</b> disponible sur de nombreux navigateurs.
        </p>
        <p class="mb-4">
            Privacy Badger est une extension qui va vous permettre de bloquer automatiquement <b>les cookies et les traqueurs</b> qui vont retourner votre chemin sur le web. Il existe d’autres extensions pertinentes pour la sécurité mais nous vous recommandons de <b>ne pas trop en rajouter</b> non plus car cela risquerait de <b>nuire à votre expérience globale</b>.
        </p>
        <img :src="`/individuals-11.png`" class="md:w-1/4 sm:w-100 mx-auto mb-4" />
        <p class="mb-4">
            Si vous avez un abonnement à un VPN il existe également des extensions pour pouvoir activer ce VPN directement depuis votre navigateur, attention toutefois le flux qui ne passera pas par le navigateur ne sera pas chiffré par le VPN !
        </p>
    </div>
</template>
