import streamlit as st
from PIL import Image

def resize_image(image_path, height, width):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    return resized_image

def app():
    images = [
        ("images/Alovera-plant.jpeg", "Aloevera", "https://www.keralaayurveda.biz/blog/aloe-vera", 
         "Aloevera, a renowned plant in Ayurveda, is prized for its soothing and healing properties for skin-related issues and internal health."),
        ("images/amla-plant.jpg", "Amla", "https://pubmed.ncbi.nlm.nih.gov/20506691/", 
         "Amla, a prized fruit in Ayurvedic tradition, is known for its exceptional antioxidant content, supporting overall health and vitality."),
        ("images/amruta_balli.png", "Amrutha Balli", "https://ayurwiki.org/Ayurwiki/Tinospora_cordifolia_-_Amrutha_balli", 
         "Amrutha Balli is renowned for the treatment of diabetes, kidney infections, asthma, cardiac conditions, amongst others. It is rich in antioxidants and has anti-viral and healing properties."),
        ("images/arali.png", "Arali", "https://en.wikipedia.org/wiki/Nerium",
         "Arali has been used to treat various ailments such as cancer, cough, cramps, diarrhea, headache, hypertension, measles, snakebite, stones, tumors, and many more."),
        ("images/ashoka.png", "Ashoka", "https://www.planetayurveda.com/library/ashoka-saraca-asoca/",
         "Ashoka tree is useful to manage female disorders like dysmenorrhea and menorrhagia due to its Vata balancing property."),
        ("images/avocado.png", "Avocado", "https://www.joyfulbelly.com/Ayurveda/ingredient/Avocado/90",
         "Avocado has been used to treat menstrual pains and cramps for ages. Also Avocado has been a great moisturizer."),
        ("images/bamboo.png", "Bamboo", "https://www.easyayurveda.com/2017/10/05/bamboo-bambusa-bambos-bans/",
         "Bamboo helps in managing acne, skin eruptions and wounds due to its anti-inflammatory and anti-bacterial properties."),
        ("images/basale.png", "Basale", "http://ccras.nic.in/content/less-known-facts-about-health-benefits-basella-alba",
         "Basale leaves and stems are used for treating boils. High quantity of Minerals, Anti oxidants prevents Anemia and osteoporosis."),
        ("images/betel.png", "Betel", "http://ccras.nic.in/content/tambulam-betel-leaf#:~:text=Uses%3A%20According%20to%20Ayurveda%2C%20Tambulasevana,boils%20and%20mouth%20ulcers%20etc.",
         "Betel is a post meal digestive stimulant, oral deodorant, natural antiseptic, astringent, diuretic, mood elevator, aphrodisiac, and nerve tonic."),
        ("images/betel-nut.png", "Betel Nut", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3892533/",
         "Betel Nuts are used for the treatment of various disorders and claimed to have detoxification, antioxidation, and antimutation properties."),
        ("images/castor.png", "Castor", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6628454/#:~:text=In%20Yunani%20medicine%2C%20castor%20root,%2C%20ascites%2C%20asthma%2C%20rheumatism%2C",
         "Castor root is used as a purgative and for skin diseases, the leaves are used to increase breastmilk production."),
        ("images/curry-leaf.png", "Curry Leaf", "https://www.planetayurveda.com/curry-leaves/",
         "Curry Leaves are used to treat various digestive problems due to their antioxidant property."),
        ("images/doddapatre.png", "Doddapatre", "https://www.slurrp.com/article/doddapatre-an-ayurvedic-antidote-to-beat-the-monsoon-blues-1691217487522",
         "Doddapatre is an effective remedy for colds, coughs, and flu. It is usually referred to as an Antidote for Monsoon Blues."),
        ("images/ekka.png", "Ekka", "https://www.urbanmali.com/blogs/wisdom/ekka-calotropis-gigantea#:~:text=Ekka%20is%20a%20natural%20remedy%20for%20cough%20and%20cold,%20and%20swelling%20in%20the%20lungs.",
         "Ekka is a natural remedy for cough and cold. It contains anti-inflammatory properties and is effective against respiratory tract infections."),
        ("images/ganike.png", "Ganike", "https://www.iafaforallergy.com/herbs-a-to-z/makoy-solanum-nigrum/",
         "Ganike has the ability to provide relief against pain and inflammation. It is also Analgesic in nature and possesses diaphoretic properties."),
        ("images/guava.png", "Guava", "https://www.planetayurveda.com/library/uses-and-benefits-of-guava/",
         "Guava leaves help to reduce bone and joint pain when applied to the affected area due to its Vata balancing property."),
        ("images/geranium.png", "Geranium", "https://www.herbalgram.org/resources/healthy-ingredients/sweet-scented-geranium/",
        "Geranium oil has been used as a pain reliever, sedative, antimicrobial, antifungal and to relieve spasms. It has also been used to help with symptoms of menopause."),
        ("images/henna.png", "Henna", "https://www.rxlist.com/henna/supplements.htm",
        "Henna is applied directly to the affected area for dandruff, fungal infections, and wounds. Henna is also used in cosmetics, hair dyes, and hair care products."),
        ("images/hibiscus.png", "Hibiscus", "https://www.keralaayurveda.biz/blog/hibiscus-for-split-ends-and-hair-loss#:~:text=Yes%2C%20the%20Hibiscus%20leaves%20and,%2C%20oils%2C%20and%20herbal%20shampoos.",
        "Classical Ayurvedic texts describe Hibiscus as Keshya, which means that it helps improve hair quality. It is also used in traditional home remedies, oils, and herbal shampoo."),
        ("images/honge.jpg", "Honge", "https://en.wikipedia.org/wiki/Pongamia",
        "Honge, an ancient Ayurvedic plant, offers potent anti-inflammatory properties, promoting overall well-being for centuries."),
        ("images/insulin.png", "Insulin", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2924971/",
        "Costus igneus, commonly known as insulin plant in India, belongs to the family Costaceae. Consumption of the leaves are believed to lower blood glucose levels."),
        ("images/jasmine.jpeg", "Jasmine", "https://en.wikipedia.org/wiki/Jasmine",
        "Jasmine, a fragrant flower cherished in Ayurveda, not only delights the senses with its scent but also provides therapeutic benefits, such as reducing stress and anxiety."),
        ("images/lemon.jpg", "Lemon", "https://en.wikipedia.org/wiki/Lemon",
        "The zesty lemon, a citrus marvel, brings a burst of refreshing flavor while delivering a rich dose of vitamin C for enhanced immunity."),
        ("images/lemongrass.jpeg", "Lemongrass", "https://en.wikipedia.org/wiki/Cymbopogon",
        "Lemongrass, a fragrant herb in Ayurveda, is prized for its calming properties, aiding in stress relief and relaxation."),
        ("images/mangoo.jpg", "Mango", "https://en.wikipedia.org/wiki/Mango",
        "The succulent mango, a tropical delight, not only tantalizes taste buds but also provides a wealth of essential vitamins and antioxidants for optimal health."),
        ("images/mint.jpg", "Mint", "https://en.wikipedia.org/wiki/Mint",
        "Mint, an invigorating herb, offers soothing relief from digestive discomfort and promotes overall digestive wellness."),
        ("images/nagadali.jpeg", "Nagadali", "https://en.wikipedia.org/wiki/Ruta_graveolens",
        "Nagadali, an Ayurvedic herb, holds potential in managing various health conditions, thanks to its diverse medicinal properties."),
        ("images/neem.jpeg", "Neem", "https://www.keralaayurveda.biz/blog/neem",
        "Neem, a versatile plant in Ayurvedic medicine, offers numerous benefits including its potent anti-inflammatory and antibacterial properties."),
        ("images/nithypusha.jpeg", "Nithyapushpa", "https://en.wikipedia.org/wiki/Catharanthus_roseus",
        "Nithyapushpa, a traditional Ayurvedic herb, plays a role in promoting general well-being through its unique properties."),
        ("images/nooni.jpg", "Nooni", "https://en.wikipedia.org/wiki/Morinda_citrifolia",
        "Nooni, an Ayurvedic ingredient, holds promise for various health benefits, contributing to holistic health practices."),
        ("images/papaya.jpg", "Papaya", "https://en.wikipedia.org/wiki/Papaya",
        "Papaya, a tropical gem, offers a bounty of vitamins and enzymes that support digestion and skin health."),
        ("images/pepper.jpg", "Pepper", "https://en.wikipedia.org/wiki/Pepper",
        "Pepper, a common spice, packs a punch with its potential to enhance digestion, metabolism, and overall health."),
        ("images/pomegrantae.jpg", "Pomegranate", "https://en.wikipedia.org/wiki/Pomegranate",
        "Pomegranate, a jewel-like fruit, boasts antioxidants and nutrients that benefit heart health and immune function."),
        ("images/rakta.jpg", "Raktachandini", "https://en.wikipedia.org/wiki/Pterocarpus_santalinus",
        "Raktachandini, an Ayurvedic herb, is recognized for its potential contributions to overall well-being."),
        ("images/rose.jpg", "Rose", "https://en.wikipedia.org/wiki/Rose",
        "The fragrant rose, celebrated in Ayurveda, not only captivates with its scent but also offers benefits for skin and emotional balance."),
        ("images/Sapota.jpeg", "Sapota", "https://en.wikipedia.org/wiki/Manilkara_zapota",
        "Sapota, a tropical delight, provides a sweet and nutritious treat, loaded with vitamins and minerals for better health."),
        ("images/Tulasi.jpg", "Tulasi", "https://en.wikipedia.org/wiki/Ocimum_tenuiflorum",
        "Tulasi, a sacred herb in Ayurveda, holds immense value for its potential to enhance immunity and alleviate respiratory issues."),
        ("images/Wood Sorrel.jpg", "Wood Sorrel", "https://www.fs.usda.gov/wildflowers/plant-of-the-week/oxalis_stricta.shtml",
        "Wood sorrel, a versatile herb, offers a range of health benefits, including aiding digestion and supporting overall wellness.")
    ]

    image_height = 300
    image_width = 300

    num_images = len(images)
    num_columns = 3
    num_rows = num_images // num_columns + (1 if num_images % num_columns != 0 else 0)

    for row in range(num_rows):
        col1, col2, col3 = st.columns(3)
        for col, image_index in zip([col1, col2, col3], range(row * num_columns, min((row + 1) * num_columns, num_images))):
            resized_image = resize_image(images[image_index][0], image_height, image_width)
            col.image(resized_image, caption=images[image_index][1], use_column_width=True)
            col.write(images[image_index][3])
            col.markdown(f"[Read More]({images[image_index][2]})")


