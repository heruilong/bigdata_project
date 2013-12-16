/**
 * Created by heruilong on 13-10-24.
 * <script src="http://code.jquery.com/jquery-1.9.1.js">
 */

alert("1");
$('#clade').change(function(){
    var selectedValue = $("#clade option:selected").text();
    if(selectedValue == "Mammal"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
    "<OPTION SELECTED VALUE='Human'>Human</OPTION>" +
    "<OPTION VALUE='Chimp'>Chimp</OPTION>" +
    "<OPTION VALUE='Gorilla'>Gorilla</OPTION>" +
    "<OPTION VALUE='Orangutan'>Orangutan</OPTION>" +
    "<OPTION VALUE='Gibbon'>Gibbon</OPTION>" +
    "<OPTION VALUE='Rhesus'>Rhesus</OPTION>" +
    "<OPTION VALUE='Baboon'>Baboon</OPTION>" +
    "<OPTION VALUE='Squirrel monkey'>Squirrel monkey</OPTION>" +
    "<OPTION VALUE='Marmoset'>Marmoset</OPTION>" +
    "<OPTION VALUE='Tarsier'>Tarsier</OPTION>" +
    "<OPTION VALUE='Mouse lemur'>Mouse lemur</OPTION>" +
    "<OPTION VALUE='Bushbaby'>Bushbaby</OPTION>" +
    "<OPTION VALUE='Tree shrew'>Tree shrew</OPTION>" +
    "<OPTION VALUE='Mouse'>Mouse</OPTION>" +
    "<OPTION VALUE='Rat'>Rat</OPTION>" +
    "<OPTION VALUE='Kangaroo rat'>Kangaroo rat</OPTION>" +
    "<OPTION VALUE='Naked mole-rat'>Naked mole-rat</OPTION>" +
    "<OPTION VALUE='Guinea pig'>Guinea pig</OPTION>" +
    "<OPTION VALUE='Rabbit'>Rabbit</OPTION>" +
    "<OPTION VALUE='Squirrel'>Squirrel</OPTION>" +
    "<OPTION VALUE='Pika'>Pika</OPTION>" +
    "<OPTION VALUE='Pig'>Pig</OPTION>" +
    "<OPTION VALUE='Alpaca'>Alpaca</OPTION>" +
    "<OPTION VALUE='Dolphin'>Dolphin</OPTION>" +
    "<OPTION VALUE='Sheep'>Sheep</OPTION>" +
    "<OPTION VALUE='Cow'>Cow</OPTION>" +
    "<OPTION VALUE='Horse'>Horse</OPTION>" +
    "<OPTION VALUE='White rhinoceros'>White rhinoceros</OPTION>" +
    "<OPTION VALUE='Cat'>Cat</OPTION>" +
    "<OPTION VALUE='Dog'>Dog</OPTION>" +
    "<OPTION VALUE='Panda'>Panda</OPTION>" +
    "<OPTION VALUE='Microbat'>Microbat</OPTION>" +
    "<OPTION VALUE='Megabat'>Megabat</OPTION>" +
    "<OPTION VALUE='Hedgehog'>Hedgehog</OPTION>" +
    "<OPTION VALUE='Shrew'>Shrew</OPTION>" +
    "<OPTION VALUE='Elephant'>Elephant</OPTION>" +
    "<OPTION VALUE='Rock hyrax'>Rock hyrax</OPTION>" +
    "<OPTION VALUE='Tenrec'>Tenrec</OPTION>" +
    "<OPTION VALUE='Manatee'>Manatee</OPTION>" +
    "<OPTION VALUE='Armadillo'>Armadillo</OPTION>" +
    "<OPTION VALUE='Sloth'>Sloth</OPTION>" +
    "<OPTION VALUE='Opossum'>Opossum</OPTION>" +
    "<OPTION VALUE='Tasmanian devil'>Tasmanian devil</OPTION>" +
    "<OPTION VALUE='Wallaby'>Wallaby</OPTION>" +
    "<OPTION VALUE='Platypus'>Platypus</OPTION>" +
    "</select>");
    } else if(selectedValue == "Vertebrate"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
        "<OPTION SELECTED VALUE='Chicken'>Chicken</OPTION>" +
        "<OPTION VALUE='Turkey'>Turkey</OPTION>" +
        "<OPTION VALUE='Zebra finch'>Zebra finch</OPTION>" +
        "<OPTION VALUE='Medium ground finch'>Medium ground finch</OPTION>" +
        "<OPTION VALUE='Budgerigar'>Budgerigar</OPTION>" +
        "<OPTION VALUE='American alligator'>American alligator</OPTION>" +
        "<OPTION VALUE='Lizard'>Lizard</OPTION>" +
        "<OPTION VALUE='Painted turtle'>Painted turtle</OPTION>" +
        "<OPTION VALUE='X. tropicalis'>X. tropicalis</OPTION>" +
        "<OPTION VALUE='Coelacanth'>Coelacanth</OPTION>" +
        "<OPTION VALUE='Tetraodon'>Tetraodon</OPTION>" +
        "<OPTION VALUE='Fugu'>Fugu</OPTION>" +
        "<OPTION VALUE='Nile tilapia'>Nile tilapia</OPTION>" +
        "<OPTION VALUE='Stickleback'>Stickleback</OPTION>" +
        "<OPTION VALUE='Medaka'>Medaka</OPTION>" +
        "<OPTION VALUE='Atlantic cod'>Atlantic cod</OPTION>" +
        "<OPTION VALUE='zebrafish'>zebrafish</OPTION>" +
        "</select>");
    } else if(selectedValue == "Deuterostome"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
        "<OPTION SELECTED VALUE='Lancelet'>Lancelet</OPTION>" +
        "<OPTION VALUE='C. intestinalis'>C. intestinalis</OPTION>" +
        "<OPTION VALUE='S. purpuratus'>S. purpuratus</OPTION>" +
        "</select>");
    } else if(selectedValue == "Insect"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
        "<OPTION SELECTED VALUE='D. melanogaster'>D. melanogaster</OPTION>" +
        "<OPTION VALUE='D. simulans'>D. simulans</OPTION>" +
        "<OPTION VALUE='D. sechellia'>D. sechellia</OPTION>" +
        "<OPTION VALUE='D. yakuba'>D. yakuba</OPTION>" +
        "<OPTION VALUE='D. erecta'>D. erecta</OPTION>" +
        "<OPTION VALUE='D. ananassae'>D. ananassae</OPTION>" +
        "<OPTION VALUE='D. pseudoobscura'>D. pseudoobscura</OPTION>" +
        "<OPTION VALUE='D. persimilis'>D. persimilis</OPTION>" +
        "<OPTION VALUE='D. virilis'>D. virilis</OPTION>" +
        "<OPTION VALUE='D. mojavensis'>D. mojavensis</OPTION>" +
        "<OPTION VALUE='D. grimshawi'>D. grimshawi</OPTION>" +
        "<OPTION VALUE='A. gamiae'>A. gamiae</OPTION>" +
        "<OPTION VALUE='A.mellifera'>A.mellifera</OPTION>" +
        "</select>");

    } else if(selectedValue == "Worm"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
        "<OPTION SELECTED VALUE='C. elegans'>C. elegans</OPTION>" +
        "<OPTION VALUE='C. brenneri'>C. brenneri</OPTION>" +
        "<OPTION VALUE='C. briggsae'>C. briggsae</OPTION>" +
        "<OPTION VALUE='C. remanei'>C. remanei</OPTION>" +
        "<OPTION VALUE='C. japonica'>C. japonica</OPTION>" +
        "<OPTION VALUE='P. pacificus'>P. pacificus</OPTION>" +
        "</select>");

    } else if(selectedValue == "Other"){
    $('#genome').replaceWith("<select id='genome' name = 'genome'>"  +
        "<OPTION SELECTED VALUE='Sea hare'>Sea hare</OPTION>" +
        "<OPTION VALUE='S. cerevisiae'>S. cerevisiae</OPTION>" +
        "</select>");
    }

});


