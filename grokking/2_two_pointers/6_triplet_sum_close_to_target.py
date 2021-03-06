# Given an array of unsorted numbers and a target number, find a triplet in the array 
# whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.

import math
import time


def print_execution_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        ts = time.time()
        _ = func(*args, **kwargs)
        print(f'Execution time {time.time() - ts}')
        return _
    return wrapper

@print_execution_time
def triplet_sum_close_to_target(nums, target):
    nums.sort()
    triplets = []
    smallest_diff = math.inf
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while(left < right):
            sum = nums[i] + nums[left] + nums[right]

            if abs(target - sum) < abs(smallest_diff):
                smallest_diff = target - sum

            
            if sum < target:
                left += 1
            else:
                right -= 1

            if smallest_diff == 0:
                break

    return target - smallest_diff


# print(triplet_sum_close_to_target([-2, 0, 1, 2], target=3))
# print(triplet_sum_close_to_target([-3, -1, 1, 2], target=1))
# print(triplet_sum_close_to_target([1, 0, 1, 1], target=100))
print(triplet_sum_close_to_target([228,306,-217,-71,770,-128,60,277,230,-383,-161,88,841,373,493,-833,898,701,-252,884,-915,-809,-743,724,324,-179,-375,497,-844,674,601,-229,-612,372,-64,-781,-87,951,741,-577,803,700,500,-866,-97,-559,697,-566,-51,38,166,-430,317,825,962,320,-705,-834,-277,-676,45,985,40,441,801,214,-583,474,-431,-700,745,836,-444,-296,400,369,206,636,42,-463,14,-156,-739,-943,662,-70,-126,957,793,602,-65,169,-978,-608,448,845,-696,-20,445,257,552,-800,140,-379,621,935,-801,-232,524,48,-761,-826,-827,-518,-841,-358,-508,-531,447,208,-511,-385,-451,575,-121,344,56,-225,-41,154,812,-640,192,95,-99,287,-878,330,449,36,-814,-522,-813,970,588,574,541,-581,131,273,-440,668,-856,-488,508,-891,-627,689,-868,-108,274,796,-181,-709,165,-455,327,710,-153,-895,922,416,-62,-748,910,877,997,-685,499,-873,115,-266,312,-312,-249,-586,-546,654,-904,528,25,-728,133,978,-392,-609,-172,376,249,529,-937,-388,15,89,-513,807,-946,886,82,735,761,729,959,13,632,-256,-344,831,-343,483,-556,-354,325,217,-76,-691,-319,696,-506,269,-485,-294,965,-775,501,-807,76,179,-538,643,-287,-958,681,940,-784,768,-36,535,-22,790,232,238,79,576,-452,-400,607,68,897,-850,-698,83,-733,579,486,-495,869,-493,495,-113,-177,-118,-681,-248,963,480,-823,-913,-510,386,699,-462,655,227,-766,252,-621,815,-334,-597,-330,-962,-23,446,800,-567,-314,-877,-163,640,433,-133,-264,-626,-973,290,924,-105,-885,-629,-136,-107,644,543,-883,-774,-145,-899,7,71,954,-929,648,932,-116,364,-253,426,818,-438,794,934,-778,-235,851,811,155,-257,-953,-928,998,615,350,926,92,769,-727,345,109,-684,-336,346,417,0,-63,973,-604,-56,200,20,510,161,685,-2,218,-776,917,308,-544,357,-724,519,-18,16,-433,-832,590,-272,93,694,-863,-554,-865,278,181,829,-475,172,-934,-189,739,240,980,-373,-892,-515,-491,-712,-159,225,-639,665,-351,949,-704,933,-57,65,742,-387,-884,340,-964,-686,-80,174,390,91,880,537,113,-407,-912,-94,788,-648,580,631,314,-199,432,-465,852,104,-932,-384,-91,-428,708,450,-646,421,805,-718,-365,260,-135,-979,971,-726,743,868,928,434,725,191,-643,792,874,331,332,703,-137,-349,3,-50,-951,559,-467,764,122,-47,-472,-647,-535,758,144,929,-352,-526,53,589,675,-215,-505,-751,-871,-947,-703,-34,150,-1000,-476,-193,-441,319,243,-688,-516,63,-168,375,195,-501,167,861,-504,-234,349,586,901,722,671,-821,-83,-127,454,494,-984,-398,946,629,-520,-353,718,148,969,-39,-763,146,715,751,359,-282,-864,894,313,-674,-157,171,827,866,-764,-171,479,-320,778,628,-447,-507,-638,-716,-3,-547,-332,-8,714,378,-738,705,335,626,-404,-289,-957,17,566,177,-54,-860,173,-982,-140,616,863,43,134,842,-812,-817,864,496,462,415,389,-158,-777,717,-887,-92,209,-988,-29,410,-975,-303,-561,64,347,748,713,-25,-889,904,-794,577,-666,-300,862,-449,-242,-362,-907,-618,723,283,112,-424,272,487,-598,719,299,-689,-908,856,-316,-243,279,-767,-558,156,944,18,-106,-714,360,342,670,905,370,994,-869,780,887,-283,-75,765,266,-468,35,-251,385,211,504,947,49,244,86,534,542,-999,-1,-411,-269,51,268,-81,-996,-98,-762,-149,979,-308,-990,-304,406,-808,-203,391,21,-896,328,489,420,213,733,545,-478,117,-768,210,-134,10,597,-672,224,285,-230,-155,-560,298,516,753,-687,-881,-187,407,-377,-971,720,571,747,-593,334,-741,-569,-634,967,539,-550,419,-454,-514,429,-750,687,736,-486,94,-965,-997,-616,-32,212,937,-960,832,883,-412,-614,-24,799,187,-579,596,564,521,66,-148,-548,-209,185,-798,247,-938,658,-576,673,-747,-785,57,706,-786,39,-539,-858,-35,-717,-805,584,142,-936,197,907,-49,820,-854,354,-389,205,762,952,-43,105,73,502,-842,54,-152,-870,-720,814,-280,808,507,490,-231,-948,-673,610,903,515,311,756,377,-980,-174,-654,773,-631,-90,-357,728,292,223,-201,-752,757,966,233,824,338,264,996,5,-12,248,513,953,-995,-167,821,-408,50,-680,915,-662,591,-216,-131,-900,611,22,-497,98,-802,-825,-196,-16,59,467,603,-939,639,-499,37,451,-744,-429,-233,-442,704,-998,547,-422,159,882,1000,553,-525,304,-653,-170,288,678,-448,-521,460,810,-255,459,-123,-810,463,565,-737,-555,289,199,392,860,-89,-124,296,-40,-78,-950,-390,902,184,-397,895,-578,514,-903,-532,444,-512,374,931,511,286,-587,637,614,634,41,606,-420,-461,28,-779,-607,690,481,653,-58,-443,-859,-879,190,-905,-848,-394,-790,925,-855,-402,968,-265,813,-773,-839,81,182], target = 3647))
print(triplet_sum_close_to_target([-907,582,312,696,-686,751,165,117,93,275,-901,-57,821,921,-133,-55,373,623,329,729,735,595,771,574,154,52,-275,-362,-819,197,-206,-829,-255,480,597,-339,-970,-992,-702,432,545,164,-203,966,-629,719,988,505,684,-557,849,-615,12,411,361,15,166,155,384,930,-83,-505,-518,-77,-740,944,-858,433,-69,-510,522,73,-879,-155,875,763,-722,-201,342,-608,314,-744,536,-571,792,107,-491,806,-534,-531,777,587,-538,-132,-222,-590,-993,-135,71,135,-695,750,-64,39,-158,598,-637,-580,382,-583,130,-689,-217,-501,64,-727,-511,-427,922,-111,564,138,-986,409,370,964,175,-312,-626,-309,651,466,908,292,-225,453,50,-862,953,-187,-760,-308,-515,439,-602,-536,524,-622,-33,532,3,-381,-123,-3,-67,682,-765,709,-253,-977,610,-122,969,-114,-585,576,-435,726,57,784,-817,-152,-188,150,991,-790,693,-855,-311,-183,276,549,-569,-390,-353,-963,711,454,66,970,92,456,496,-728,58,237,-844,747,643,-522,-80,136,-918,26,0,-625,631,10,-932,961,-299,-665,-213,-821,-973,14,94,-895,-926,258,339,-383,556,-30,879,-317,-467,-403,701,338,859,483,-881,-472,-273,687,578,-391,566,-17,-343,-239,786,142,710,788,277,252,-568,-954,901,867,182,-827,525,428,-934,83,25,-508,104,-659,-843,-910,-452,-238,-485,-955,124,520,-656,629,-209,-666,-710,633,552,-733,743,464,-36,654,-240,269,213,87,-1000,114,-714,-7,504,628,-408,422,-507,-97,429,-997,810,268,259,501,-874,-935,48,-610,353,33,-423,-261,-335,-173,-489,977,61,727,-868,844,-332,605,-216,-526,249,406,-742,335,-74,638,43,-1,889,523,-634,272,601,-499,-49,-270,398,-591,869,910,-46,435,-453,-699,16,450,385,394,-288,769,-700,-345,-124,-917,567,519,-784,-976,242,987,-2,-547,613,-321,485,-600,-775,-777,-417,65,554,186,-770,706,-552,305,645,293,686,-334,195,656,700,233,762,577,380,-542,979,876,-841,-743,-751,-635,-454,-857,158,795,-90,495,-737,-15,201,334,-244,-815,894,-39,300,352,34,-11,-153,-838,652,-219,-58,-267,-648,518,-296,-177,-741,-150,717,408,-232,-231,-387,-415,56,350,-886,253,367,395,824,572,-54,714,215,-14,-999,-911,470,962,279,848,823,286,858,-549,-214,-523,569,-748,754,307,360,-372,479,-481,-776,766,510,-437,-421,-286,-532,860,-32,-167,801,68,-468,-99,915,313,-773,-671,996,-820,281,-593,-466,-229,-643,139,299,-329,972,-517,-333,120,198,707,-246,-889,648,-305,-783,674,959,333,-938,692,998,193,118,-559,606,28,-707,-832,171,-9,828,-247,374,839,586,817,221,153,-148,-208,306,635,835,244,756,330,283,-48,-496,-752,-119,270,170,-277,-480,561,-905,-971,345,85,-388,112,19,324,127,-199,899,-112,796,-840,-951,-493,404,-897,-218,-38,49,53,658,-645,-426,632,-611,-287,512,-563,745,-207,207,-814,688,900,857,-262,377,-847,-555,722,59,376,-117,926,-215,533,-869,97,-424,-113,-588,-47,797,-18,-543,665,583,274,-230,-409,-592,880,-245,791,-609,916,-612,755,691,956,-456,-980,-586,-202,-328,-276,591,842,327,-352,18,163,-24,-937,223,-771,-393,773,-806,151,-65,862,-650,-786,322,-965,-670,-616,-94,72,364,-175,386,-260,-859,-371,-798,-250,46,837,-210,219,770,443,131,618,282,666,-169,-439,-26,152,303,-290,-825,11,-205,502,893,581,664,-831,744,-354,-43,-974,391,291,679,-667,-358,35,-794,-813,620,-715,-242,-392,-662,-405,799,-91,-193,720,469,-731,937,-498,866,-761,20,-848,424,-170,-360,653,-692,-400,-562,-982,816,-194,-256,508,-476,-433,542,819,-947,265,630,-436,-837,-527,-223,511,2,-854,793,-198,-21,-41,-258,-658,548,226,-931,-729,-785,128,-684,-620,820,-323,-639,514,-621,-165,414,-455,477,-268,-871,982,264,7,-53,-513,251,-939,-913,-655,-792,-369,832,699,-429,-86,948,995,-736,-474,-368,-735,471,474,507,-484,452,-34,-631,-252,187,789,-300,-475,619,-799,-189,-279,728,-688,-778,-108,-884,296,807,-584,184,70,-892,379,105,-292,455,6,176,-71,-149,517,-103,-180,994,344,-726,280,210,-553,-763,-863,-303,-22,-678,-860,-271,236,681,-92,-754,91,412,-464,457,-624,-338,-646,418,941,818,615,624,-344,326,513,-364,781,-876,-972,-84,-861,-266,-115,-116,-349,-434,509,-969,660,381,676,78,-550,718,-399,315,-640,-676,-473,-425,-341,304,401,-37,690,885,850,898,-681,870,423,321,-357,705,625,855,-168,-25,-234,-604,188,-340,-912,798,351,284,290,-181,-459,831,203,809,721,733,776,736,958,800,-720,644,40,-160,-220,678,634,-850,-644,813,472,-487,698,723,-224,1,247,-787,132,-554,826,-129,-578,396,642,732,-835,616,768,-102,-599,403,-185]
, -5698))






