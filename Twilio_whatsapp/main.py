from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app= Flask(__name__)

@app.route('/bot',methods=['POST'])
def bot():
    user_msg=request.values.get('Body','').lower()
    user_msg1=request.values.get('Body','').lower()
    bot_resp=MessagingResponse()
    msg=bot_resp.message()
    
    if 'hello' in user_msg:
            msg.body("Hi there! How may I help you?")
    elif '1' in user_msg:
        msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/333/original/1303616796_a8af71b884_z.jpg")
        msg.body("Hello There, Welcome to Urban Farm. What would you like to know about maize.Give us a feedback on the chat below.\nA.Maize Description\n B.Maize Plantation\nC.Maize Maintenance\n C D.Maize Diseases.\n")
    elif 'a' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/333/original/1303616796_a8af71b884_z.jpg")
            msg.body("The maize plant possesses a simple stem of nodes and internodes. A pair of large leaves extend off of each internode and the leaves total 8–21 per plant. The leaves are linear or lanceolate (lance-like) with an obvious midrib (primary vein) and can grow from 30 to 100 cm (11.8–39.4 in) in length. The male and female inflorescences (flower bearing region of the plant) are positioned separately on the plant. The male inflorescence is known as the tassel while the female inflorescence is the ear. The ear of the maize is a modified spike and there may be 1–3 per plant. The maize grains, or kernels, are encased in husks and total 30–1000 per ear. The kernels can be white, yellow, red, purple or black. Maize is an annual plant, surviving for only one growing season and can reach 2–3 m (7–10 ft) in height")
    elif 'b' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/333/original/1303616796_a8af71b884_z.jpg")
            msg.body("Maize is best grown in warm, tropical and sub-tropical regions as it requires warm soils to develop optimally. One of the most important requirements for growing maize is a high quality soil which is deep, fertile and well-draining with a pH between 6.0 and 6.8. Maize plants are very heavy feeders and even the most fertile of soils may need to supplemented with nutrients as the plants develop, particularly nitrogen. Maize also requires plenty of space as it grows and is pollinated by wind. It should be planted where it will receive full sunlight for most of the day and provided with ample moisture.")
            msg.body("Planting dates for maize depend on the variety being grown. Standard varieties should be planted when the soil has warmed to at least 12.7°C (55°F) and supersweet varieties when the soil reaches 18.3°C (65°F). Soil can be brought up to temperature faster by laying black plastic mulches approximately 1 week prior to planting. Seeds should be sown about 2.5 cm (1 in) deep and 10–15 cm (~3–4 in) apart allowing 76–91 cm (~30–36 in) between rows. Maize should be planted in blocks (numerous rows) rather than in a single long row as it is wind pollinated and pollen can transfer between plants much more efficiently. Seedlings should be thinned to a final spacing 20–30 cm (8–12 in) when they are approximately 7.5–10.0 cm (3–4 in) in height. It is common to stagger maize plantings to ensure a continuous harvest over the summer months")
    elif 'c' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/336/original/5365524-SMPT.jpg")
            msg.body("Maize plants are heavy feeders, particularly of nitrogen (N) and care should be taken to provide them with adequate nutrients by applying fertilizer. Maize undergoes a rapid growth period between 30 and 40 days after planting and should be fertilized just before this. All fertilizer applications should be made before the tasseling period to ensure the plant maximizes nitrogen use. Be aware of symptoms of nutrient deficiency, plants should be a deep green color. Purple tinged leaves indicate that the plants are suffering from a lack of phosphorous, whereas light green leaves indicate a lack of nitrogen. Apply fertilizer. Plants also require adequate soil moisture throughout the growing period in order to tassel and form silks. Soaker hoses can be used to great effect in small to mid-size plantings. Pollination occurs when pollen is transferred from the male tassel to the female silk by the wind. Each silk produced a single kernel of corn and partially filled ears are usually a result of poor pollination.")
    elif 'd' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/001/130/original/Cercospora_leaf_spot_4.jpg")
            msg.body("Plant corn hybrids with resistance to the disease; crop rotation and plowing debris into soil may reduce levels of inoculum in the soil but may not provide control in areas where the disease is prevalent; foliar fungicides may be economically viable for some high yeilding susceptible hybrids")
            msg.body("More images and details of diseases at PlantVillage.co.ke or UrbanCrop.co.ke")
            
            
            
            
            
            
            
            # BEANS
            
    elif '2' in user_msg:
        msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/381/original/4947491450_1669cdb4ab_z.jpg")
        msg.body("Hello There, Welcome to Urban Farm. What would you like to know about Beans.Give us a feedback on the chat below.\nE.Beans Description\n F.Beans Plantation\nG.Beans Maintenance\n C H.Beans Diseases.\n")
    elif 'e' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/381/original/4947491450_1669cdb4ab_z.jpg")
            msg.body("Beans are crop which are grown as a pulse and green vegetable. The common bean can be bushy, vine-like or climbing depending on the variety being grown. The leaves grow alternately on the stems, are green or purple in color and are divided into 3 oval leaflets with smooth edges. The leaves can grow 6–15 cm (2.4–5.9 in) long and 3–11 cm (1.2–4.3 in) wide. The common bean produces white, pink, lilac or purple flowers which are approximately 1 cm (0.4 in) in diameter, and bean pods 8–20 cm (3.1–7.9 in) long and 1–1.5 cm (0.4–0.6 in) wide which can range in color from green to yellow or black to purple. Each pod contains 4-6 smooth, kidney-shaped beans. Common bean plants are annual plants and last only one growing season and range greatly in size from the bushy varieties 20–60 cm (7.9–24 in) in height; to vines or runner beans which can reach 2–3 m (6 ft 7 in–9 ft 10 in) in length")
    elif 'f' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/387/original/5027699128_fdd023b992_z.jpg")
            msg.body("Basic requirements Common beans are warm-season crops and should be planted after all danger of frost has passed and the soil has warmed. Beans will grow best at soil temperatures between 15.5 and 29°C (60–85°F) and are sensitive to cold temperatures and frosts. Beans will grow best in a fertile, well-draining soil with a pH between 6.0 and 6.75 Beans will perform best in full sunlight. Varieties Common beans can either be bush or pole varieties. Bush beans will grow erect without any support and require less care than pole varieties. Pole beans grow vertically on a support and are generally easier to harvest. Most type of bean are now available as both bush and pole varieties. Some green bean varieties may be referred to as “string” beans. This name is a reference to older varieties which produced a stringy fibre along the seam of the pod. Modern cultivars were bred which did not produce this substance and which are commonly referred to as “snap” beans due to the ease with which the green pods can be snapped in two.")
    elif 'g' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/452/original/3280201047_85df92de30_z.jpg")
            msg.body("Beans should be direct seeded in the garden in when the soil has reached a temperature of at least 15.5°C (60°F), with the optimum temperature for germination being between 15.5 and 29°C (60–85°F). Planting at cooler temperatures leads to slow germination and promotes seed rotting. Seeds should be planted 2.5–3.5 cm (1–1.5 in) deep. Bush beans should be planted 5–10 cm (2–4 in) apart allowing 0.6–0.9 m ( 2–3 ft) between rows. Pole beans can be planted in both row and hills. In rows, seeds should be spaced 15–25 cm (6–10 in) apart allowing 0.9–1.2 m (3–4 ft) between rows. For a continuous harvest of beans over the summer months, make new plantings every 2–3 weeks.Beans are generally ready for harvest approximately two weeks after bloom. The beans should be harvested just before the seeds are mature and before they form bumps on the pod. The pods should be firm and snap when they are bent. Pick beans every 2–3 days to ensure the plants remain productive. Pinch beans rather than pulling to avoid damaging the plant. Cut pole beans from the plant using scissors.")
    elif 'h' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/000/602/original/Alternaria_leaf_spot.jpg")
            msg.body("Plant beans in fertile soil; foliar fungicide application may be required.Plant resistant varieties; use certified disease free seed; avoid sprinkler irrigation, water plants at base; plow bean crop debris into soil.")
            msg.body("More images and details of diseases at PlantVillage.co.ke or UrbanCrop.co.ke")
            
            
            
            
            
            
            # Wheat
            
    elif '3' in user_msg:
        msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/781/original/5417132620_39204e0cd2_z.jpg")
        msg.body("Hello There, Welcome to Urban Farm. What would you like to know about Wheat.Give us a feedback on the chat below.\nI.Wheat Description\n J.Wheat Plantation\nK.Wheat Maintenance\n C L.Wheat Diseases.\n")
    elif 'i' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/781/original/5417132620_39204e0cd2_z.jpg")
            msg.body("Wheat, is the name given to several plants in the genus Triticum including Triticum aestivum, Triticum compactum, Triticum spelta and Triticum durum, which are annual or biennial grasses grown primarily for their grain. Wheat species possess an erect smooth stem with linear leaves that grow in two rows on either side of the stem with larger 'flag' leaves at the top of the stem. The stem terminates in a spike that is made up on individual spikelets, each possessing 3–9 florets. The wheat fruit develops within the spikelets, maturing to a seed (kernel). Wheat can reach 1.2 m (4 ft) in height and like other cereals, has been developed into different varieties that are adapted to planting at different times of the year. Spring wheat is planted for a late summer harvest, whereas Winter wheat is planted for harvesting in early to mid summer. Overwintering varieties are more commonly grown in regions with mild winters.Wheat is one of the most important food plants in the world. It is used primarily to produce flour for bread. It is used widely in the production of many other baked goods. Wheat grain is also used in the manufacture of alcoholic beverages and alcohol. Wheat straw is used as an animal feed and in the manufacture of carpets, baskets, packing, bedding, and paper.")
    elif 'j' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/779/original/8554467065_f0ae6d9264_z.jpg")
            msg.body("Wheat varieties One of the first things to consider before planting is which type of wheat you want to grow. There are several different varieties to choose from depending on the time of year and how you want to utilize your harvest. Wheat is broadly categorized into Winter wheat and Spring wheat. Winter wheat is high yielding and is planted in the Fall and harvested in the Spring or Summer of the following year (depending on location). Spring wheat is not as high yielding but tolerated drier conditions. It is planted in the Spring and harvested in the Fall. Both Spring and Winter wheat is then further categorized as soft wheat, hard wheat, spelt or durum.General requirements Wheat can be grown in a wide variety of climates but grows best in cool regions where the temperature is between 10 and 24°C (50–75°F). Wheat will not grow at temperatures above 35°C (95°F). Wheat will grow optimally in a deep, fertile, well draining and well aerated soil at a pH between 5.5 and 7.5.")
            # msg.body("Planting Winter wheat varieties should be planted in the Fall approximately 6 to 8 weeks before the first frost date. Spring wheat varieties should be planted as soon as the soil can be worked in the Spring. Commercially grown wheat is usually mechanically drilled using a machine that creates a furrow and drops the seed in before covering it back up. Wheat seeds can be sown by hand broadcasting in smaller areas, or using a hand-cranked seeder. Seeds are usually sown to at depths ranging from 2 to 12 cm (0.8–4.7 in) depending on soil conditions (seed must be sown deeper in drier soil). Once the seeds have been scattered, the soil should be raked lightly to set the seeds at the desired depth.")
    elif 'k' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/785/original/800px-The_combine_Claas_Lexion_584_in_the_wheat_harvest.jpg")
            msg.body("Wheat can be grown in a wide variety of climates but grows best in cool regions where the temperature is between 10 and 24°C (50–75°F). Wheat will not grow at temperatures above 35°C (95°F). Wheat will grow optimally in a deep, fertile, well draining and well aerated soil at a pH between 5.5 and 7.5.Wheat is ready to harvest when the stalks and heads have turned from green to yellow and the seed heads are drooping towards the ground. Check the seeds for ripeness before harvest. The should be firm and crunchy and not doughy in texture. Commercially produced wheat is usually harvested using a combine. Smaller plots can be harvested by hand using a scythe or sickle. Small plots can be harvested by snipping off the heads with a pair of scissors.")
    elif 'l' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/000/975/original/Bacterial_streak_1.jpg")
            msg.body("Avoid planting seed from infected fields; avoid overhead irrigation; plant less susceptible cultivars.Avoid planting seed from plants grown in fields where the disease is known to be present")
            msg.body("More images and details of diseases at PlantVillage.co.ke or UrbanCrop.co.ke")
              
            
            
            # Banana
            
    elif '4' in user_msg:
        msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/745/original/3229575322_e8929750c5_z.jpg")
        msg.body("Hello There, Welcome to Urban Farm. What would you like to know about Wheat.Give us a feedback on the chat below.\nM.Banana Description\n N.Banana Plantation\nO.Banana Maintenance\n C P.Banana Diseases.\n")
    elif 'm' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/745/original/3229575322_e8929750c5_z.jpg")
            msg.body("is the world's largest herbaceous perennial plant and belongs to the family Musaceae. It is grown for it's fleshy, curved banana fruit. The plant is tall, tropical and tree-like with a sturdy main pseudostem (not a true stem as it is made of rolled leaf bases) with the leaves arranged spirally at the top. The leaves are large blades with a pronounced central midrib and obvious veins. They can reach up to 2.7 m (8.9 ft) in length and up to 0.6 m (2.0 ft) in width. Each pseudostem produces a group of flowers which may also be called the 'banana heart' from which the fruits develop in an hanging cluster. The banana fruits are comprised of a protective outer layer, or skin, with numerous long, thin strings that run between the skin and the edible inner portion. The seeds are tiny black specks running through the center of the fruit. In commercial plantations, the parent banana plant dies after harvest and is replaced with a daughter plant. However, a plantation can grow for 25 years or more if managed properly. The trees can reach heights between 2 and 9 m")
    elif 'n' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/002/748/original/5680834277_b11b595c96_z.jpg")
            msg.body("Basic requirements Bananas grow best in hot and humid climates, require a rainfall of at least 1000 mm (39.4 in) per year to survive and have a high light requirement. Banana plants grow optimally at 27°C (98.6°F) and require a deep soil, rich in organic matter which is well draining and well aerated. The plants will grow optimally in soil with a pH between 5.5 and 7.0. Young banana plants are very susceptible to wind damage and it is recommended that they are planted in sufficient shelter or in a block so that the plants will protect one another. ")
            # msg.body("Planting Winter wheat varieties should be planted in the Fall approximately 6 to 8 weeks before the first frost date. Spring wheat varieties should be planted as soon as the soil can be worked in the Spring. Commercially grown wheat is usually mechanically drilled using a machine that creates a furrow and drops the seed in before covering it back up. Wheat seeds can be sown by hand broadcasting in smaller areas, or using a hand-cranked seeder. Seeds are usually sown to at depths ranging from 2 to 12 cm (0.8–4.7 in) depending on soil conditions (seed must be sown deeper in drier soil). Once the seeds have been scattered, the soil should be raked lightly to set the seeds at the desired depth.")
    elif 'o' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/003/692/original/5681398178_007f1d6114_z.jpg")
            msg.body("Planting The desired pieces of the plant are usually planted 30–60 cm (11.8–23.6 in) deep in the soil and should generally be planted at the end of the dry season or the beginning of the wet season. Plant spacing is dependent on the cultivar being planted. Frequent weeding is required until plants are tall enough to shade out competing plants and should be started about 6 weeks after planting. The banana plants are fast growing and require the frequent addition of nutrients as well as additional irrigation in the dry season. Banana is often grown alongside other crop plants with similar requirements, indeed, the young banana plants make excellent 'nurses' for other crops such as papaya or cocoa which can be grown very close to the young banana.")
    elif 'p' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/003/483/original/5671043104_071aa2c3c8_z.jpg")
            msg.body("Commercially produced fruit should be washed and dipped in fungicide prior to shipping; protect fruit from injury; remove flower parts which can harbour fungus.Export plantations may require regular fungicide applications; increase plant spacing to improve air circulation and reduce humidity; remove leaves with mature spots")
            msg.body("More images and details of diseases at PlantVillage.co.ke or UrbanCrop.co.ke")
            
            
            
            
            # Sugarcane
            
    elif '5' in user_msg:
        msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/004/894/original/11301704955_0b82eae64a_z.jpg")
        msg.body("Hello There, Welcome to Urban Farm. What would you like to know about Wheat.Give us a feedback on the chat below.\nQ.Sugarcane Description\n R.Sugarcane Plantation\nS.Sugarcane Maintenance\n C T.Sugarcane Diseases.\n")
    elif 'q' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/004/894/original/11301704955_0b82eae64a_z.jpg")
            msg.body("Sugarcane, Saccharum officinarum, is a perennial grass in the family Poaceae grown for its stem (cane) which is primarily used to produce sucrose. Sugarcane has a thick, tillering stem which is clearly divided into nodes and internodes. The leaves of the plant grow from the nodes of the stem, arranged in two rows on either side of the stem. The leaves are tubular and blade-like, thicker in the centres than at the margins and encircle the stem. The inflorescence of sugarcane is a terminal panicle which possesses two spikelets and seeds protected by husks (glumes) covered in silky hair. Two flowers are produced on the inflorescence, one sterile and the other bisexual. Sugarcane can reach a height of up to 6 m (3.3 ft) and once harvested, the stalk will regrow allowing the plant to live for between 8 and 12 years.Sugarcane is primarily used for the production of cane sugar (sucrose). One of the biproducts of sugarcane production is bioethanol which can be used as a fuel in place of gasoline. The dried fibre which is left over after the extraction of the sugarcane juice is called bagasse and is used in paper and textile production, as a fuel or as an organic mulch.")
    elif 'r' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/004/892/original/8266592682_fc84edb59d_z.jpg")
            msg.body("Basic requirements Sugarcane grows best in tropical and subtropical regions as the plants require a warm, sunny and moist environment for growth. Plants will grow optimally at temperatures between 26 and 33°C Setts should be cut from carefully selected mature canes. A few days before the cuttings are taken, the end of the canes are removed to break the apical dominance of the cane and promote the breaking of buds. The best cuttings are taken from the upper portions of the cane and should be approximately 40 cm (16 in) in length with 2–3 buds. Sugarcane setts should be planted horizontally or at a 45° angle in furrows 15–30 cm (6–12 in) deep. Once in the ground, the setts should be covered with a thin layer of soil. Setts can be grown in a nursery bed and transplanted to the field or planted directly at the final growing site. The average planting density for sugarcane is 15,000–24,000 cuttings per hectare of land. Normally furrow method of planting is followed. A new method called pit method of planting promises two to three times more yield and more ratoon (up to 10) compared to furrow method.")
            
    elif 's' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/003/692/original/5681398178_007f1d6114_z.jpg")
            msg.body("General care and maintenance Plantations should be kept free from weeds with weeding being carried out every 3–4 weeks. Weeds can be removed by hand or through the use of machinery or appropriate chemicals. If rainfall is not sufficient to meet the growth requirements of the plants then irrigation must be supplied every 2–4 weeks through furrow or sprinkler irrigation. Soil should be mounded up around the base of the canes 1–2 times during the growing season to promote good root development, aid drainage in heavy soil or prevent lodging in light soils. ")
    elif 't' in user_msg:
            msg.media("https://plantvillage-production-new.s3.amazonaws.com/images/pics/000/004/894/original/11301704955_0b82eae64a_z.jpg")
            msg.body("Disease can be controlled through the application of appropriate foliar fungicides.")
            msg.body("More images and details of diseases at PlantVillage.co.ke or UrbanCrop.co.ke")
              
              
           
    return str(bot_resp) 

if __name__ == '__main__':
    app.run(debug=True)

        
    
                
            