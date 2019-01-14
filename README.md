<meta class="export" charset="utf-8">
<style class="export">
	* { margin: 0; padding: 0; font-family: sans-serif; }
	ul[contenteditable="true"] { border: 4px groove; }
	li:first-child { background: aliceblue; border: 1px solid white; font-weight: bold; padding: .5em; }
	li { padding: .3em; padding-left: 1em; }
</style>
<style class="export">
	main {	height: calc(100vh - 15vh); width: calc(65vh - 15vh);   
			border: solid black; border-width: 7.5vh 2vh 7.5vh; border-radius: 2vh;
			font-size: 2.5vh; overflow: auto; }
	li:before { content: '\2610\a0'; }
	li[active]:before { content: '\2611\a0'; } 
	li:first-child:before { content: ''; }
	li:first-child[onclick="collapse(this)"] ~ * { display: inherit; }
	li:first-child[onclick="expand(this)"] ~ * { display: none; }
	li:first-child[onclick="expand(this)"] ~ *[active] { display: block; }
</style>
<script class="export">
onload = function (){
	if(localStorage.getItem('checklist'))
		document.body.innerHTML = localStorage.getItem('checklist');
	for(var x of document.querySelectorAll('[onclick="collapse(this)"]'))
		collapse(x);
}
save = function(){
	console.log('save');
	localStorage.setItem('checklist', document.body.innerHTML);
}
activate = function (item){
	if(item.getAttribute('active'))
		item.removeAttribute('active');
	else
		item.setAttribute('active', true);
	save();
}
expand = function (group){
	group.setAttribute("onclick", "collapse(this)");
}
collapse = function (group){
	if(group.getAttribute("contenteditable")!="true")
		group.setAttribute("onclick", "expand(this)");
}
edit = function (event){
	event.preventDefault();
	var x = event.target;
	var g = getGroup(x);
	if(g.getAttribute("contenteditable")!="true"){
		g.setAttribute("contenteditable", true);
		g.focus();
		expand(x);
	}else{
		g.removeAttribute("contenteditable");
		collapse(x);
		save();
	}
}
getGroup = function (x){
	while(x.tagName && x.tagName!='UL')
		x = x.parentElement;
	return x;
}
</script>
<main class="export">
	
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Crémerie</li>
		<li onclick="activate(this)">œufs</li>
		<li onclick="activate(this)">beurre</li>
		<li onclick="activate(this)">crème fraiche</li>
		<li onclick="activate(this)">fromage</li>
		<li onclick="activate(this)">gruyère râpé</li>
		<li onclick="activate(this)">yaourts</li>
		<li onclick="activate(this)">pâte à tarte</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Viande</li>
		<li onclick="activate(this)">bœuf</li>
		<li onclick="activate(this)">veau</li>
		<li onclick="activate(this)">porc</li>
		<li onclick="activate(this)">volailles</li>
		<li onclick="activate(this)">lardons</li>
		<li onclick="activate(this)">jambon</li>
		<li onclick="activate(this)">charcuterie</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Poisson</li>
		<li onclick="activate(this)">saumon fumé</li>
		<li onclick="activate(this)">bâtons de crabe</li>
		<li onclick="activate(this)">crevettes</li>
		<li onclick="activate(this)">moules</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Fruits/Légumes</li>
		<li onclick="activate(this)">pommes</li>
		<li onclick="activate(this)">poires</li>
		<li onclick="activate(this)">bananes</li>
		<li onclick="activate(this)">citron</li>
		<li onclick="activate(this)">salade</li>
		<li onclick="activate(this)">tomates</li>
		<li onclick="activate(this)">carottes</li>
		<li onclick="activate(this)">pommes de terre</li>
		<li onclick="activate(this)">oignons</li>
		<li onclick="activate(this)">ail/échalote</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Conserves</li>
		<li onclick="activate(this)">maïs</li>
		<li onclick="activate(this)">petits pois</li>
		<li onclick="activate(this)">haricots verts</li>
		<li onclick="activate(this)">sauce tomate</li>
		<li onclick="activate(this)">thon</li>
		<li onclick="activate(this)">terrines</li>
		<li onclick="activate(this)">olives</li>
		<li onclick="activate(this)">cornichons</li>
		<li onclick="activate(this)">plats cuisinés</li>
		<li onclick="activate(this)">fruits en sirop</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Épicerie</li>
		<li onclick="activate(this)">pâtes</li>
		<li onclick="activate(this)">riz</li>
		<li onclick="activate(this)">lentilles</li>
		<li onclick="activate(this)">purée</li>
		<li onclick="activate(this)">soupe</li>
		<li onclick="activate(this)">croutons</li>
		<li onclick="activate(this)">chapelure</li>
		<li onclick="activate(this)">bouillon cube</li>
		<li onclick="activate(this)">épices</li>
		<li onclick="activate(this)">poivre/sel</li>
		<li onclick="activate(this)">moutarde</li>
		<li onclick="activate(this)">mayonnaise</li>
		<li onclick="activate(this)">huile</li>
		<li onclick="activate(this)">vinaigre</li>
		<li onclick="activate(this)">farine</li>
		<li onclick="activate(this)">sucre</li>
		<li onclick="activate(this)">sucre vanillé</li>
		<li onclick="activate(this)">levure</li>
		<li onclick="activate(this)">pain</li>
		<li onclick="activate(this)">gâteaux apéro</li>
		<li onclick="activate(this)">chips</li>
		<li onclick="activate(this)">cacahuètes</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Petit-déj'/goûter</li>
		<li onclick="activate(this)">café</li>
		<li onclick="activate(this)">cacao</li>
		<li onclick="activate(this)">thé/tisane</li>
		<li onclick="activate(this)">céréales</li>
		<li onclick="activate(this)">confiture</li>
		<li onclick="activate(this)">miel</li>
		<li onclick="activate(this)">pâte à tartiner</li>
		<li onclick="activate(this)">brioche</li>
		<li onclick="activate(this)">biscottes</li>
		<li onclick="activate(this)">pain de mie</li>
		<li onclick="activate(this)">gâteaux</li>
		<li onclick="activate(this)">chocolat</li>
		<li onclick="activate(this)">chewing-gum</li>
		<li onclick="activate(this)">dosettes café</li>
		<li onclick="activate(this)">filtres à café</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Bébé</li>
		<li onclick="activate(this)">lait</li>
		<li onclick="activate(this)">biscuits</li>
		<li onclick="activate(this)">petits pots</li>
		<li onclick="activate(this)">compotes</li>
		<li onclick="activate(this)">couches</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Hygiène</li>
		<li onclick="activate(this)">savon</li>
		<li onclick="activate(this)">brosse à dents</li>
		<li onclick="activate(this)">dentifrice</li>
		<li onclick="activate(this)">coton</li>
		<li onclick="activate(this)">coton-tige</li>
		<li onclick="activate(this)">gel douche</li>
		<li onclick="activate(this)">déodorant</li>
		<li onclick="activate(this)">shampoing</li>
		<li onclick="activate(this)">démêlant</li>
		<li onclick="activate(this)">gel coiffant</li>
		<li onclick="activate(this)">rasoirs/lames</li>
		<li onclick="activate(this)">mousse à raser</li>
		<li onclick="activate(this)">après-rasage</li>
		<li onclick="activate(this)">crème</li>
		<li onclick="activate(this)">démaquillant</li>
		<li onclick="activate(this)">dissolvant</li>
		<li onclick="activate(this)">tampons</li>
		<li onclick="activate(this)">serviettes</li>
		<li onclick="activate(this)">cire dépilatoire</li>
		<li onclick="activate(this)">mouchoirs</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Pharmacie</li>
		<li onclick="activate(this)">alcool 90°</li>
		<li onclick="activate(this)">pansements</li>
		<li onclick="activate(this)">produit lentille</li>
		<li onclick="activate(this)">désinfectant</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Entretien</li>
		<li onclick="activate(this)">éponges</li>
		<li onclick="activate(this)">sac poubelle</li>
		<li onclick="activate(this)">film étirable</li>
		<li onclick="activate(this)">papier alu</li>
		<li onclick="activate(this)">essuie-tout</li>
		<li onclick="activate(this)">eau de javel</li>
		<li onclick="activate(this)">lingettes</li>
		<li onclick="activate(this)">anticalcaire</li>
		<li onclick="activate(this)">gel WC</li>
		<li onclick="activate(this)">produit sol</li>
		<li onclick="activate(this)">spray vitre</li>
		<li onclick="activate(this)">liquide vaisselle</li>
		<li onclick="activate(this)">lave-vaisselle</li>
		<li onclick="activate(this)">tablettes/sel</li>
		<li onclick="activate(this)">lessive</li>
		<li onclick="activate(this)">adoucissant</li>
		<li onclick="activate(this)">cirage</li>
		<li onclick="activate(this)">engrais</li>
		<li onclick="activate(this)">insecticide</li>
		<li onclick="activate(this)">papier toilette</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Animaux</li>
		<li onclick="activate(this)">croquette</li>
		<li onclick="activate(this)">boîtes</li>
		<li onclick="activate(this)">litière</li>
		<li onclick="activate(this)">jouet</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Surgelés</li>
		<li onclick="activate(this)">glaces</li>
		<li onclick="activate(this)">légumes</li>
		<li onclick="activate(this)">frites</li>
		<li onclick="activate(this)">pizza</li>
		<li onclick="activate(this)">poissons panés</li>
		<li onclick="activate(this)">steak hachés</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Boissons</li>
		<li onclick="activate(this)">eau</li>
		<li onclick="activate(this)">eau gazeuse</li>
		<li onclick="activate(this)">lait</li>
		<li onclick="activate(this)">jus de fruits</li>
		<li onclick="activate(this)">sodas</li>
		<li onclick="activate(this)">sirop</li>
		<li onclick="activate(this)">bières</li>
		<li onclick="activate(this)">vin</li>
		<li onclick="activate(this)">apéritifs</li>
	</ul>
	<ul oncontextmenu="edit(event)">
	<li onclick="expand(this)">Maison</li>
		<li onclick="activate(this)">serviettes</li>
		<li onclick="activate(this)">piles</li>
		<li onclick="activate(this)">ampoules</li>
		<li onclick="activate(this)">bougies</li>
		<li onclick="activate(this)">stylo/crayon</li>
		<li onclick="activate(this)">colle</li>
		<li onclick="activate(this)">ruban adhésif</li>
		<li onclick="activate(this)">enveloppes</li>
		<li onclick="activate(this)">timbres</li>
	</ul>
</main>
