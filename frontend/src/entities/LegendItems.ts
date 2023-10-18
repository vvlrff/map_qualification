import LegendItem from "./LengendItem";

let legendItems = [

  new LegendItem(
    "8+",
    "#8b0000",
    (cases) => cases > 7
  ),

  new LegendItem(
    "5-7",
    "#9e2a2a",
    (cases) => cases > 4 && cases <= 7
  ),

  new LegendItem(
    "2-4",
    "#c57f7f",
    (cases) => cases >= 2 && cases <= 4
  ),

  new LegendItem(
    "1",
    "#ebd4d4",
    (cases) => cases === 1
  ),

  new LegendItem(
    "0", 
    "#ffffff", 
    (cases) => cases === 0
  ),
];

export default legendItems;

/**
 * 7 > 1 million                        #8b0000
 * 6 >= 500 thousand < 1 million        #9e2a2a
 * 5 >= 200 thousand < 500 thousand     #b15555
 * 4 >= 100 thousand  < 200 Thousand    #c57f7f
 * 3 > 50 thousand < 100 thousand       #d8aaaa
 * 2 >= 0 < 50 thousand                 #ebd4d4
 * 1 NO DATA                            #ffffff
 */

/*

#741f1f // Really red
#9c2929 // more red
#c57f7f // red
#d8aaaa //more pink
#ebd4d4 //pink
#ffffff //white
*/
