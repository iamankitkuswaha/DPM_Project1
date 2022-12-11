// Social Medial links:

// whatsapp:
// https://api.whatsapp.com/send?text=[post-title] [post-url]

// facebook:
// https://www.facebook.com/sharer.php?u=[post-url]

// twitter:
// https://twitter.com/share?url=[post-url]&text=[post-title]&via=[via]&hashtags=[hashtags]

// Linkedin:
// https://www.linkedin.com/shareArticle?url=[post-url]&title=[post-title]


const facebookBtn = document.querySelector(".facebook-btn");
const twitterBtn = document.querySelector(".twitter-btn");
const whatsappBtn = document.querySelector(".whatsapp-btn");
const linkedinBtn = document.querySelector(".linkedin-btn");

function init(){
    console.log("Hello"); 
    const generatedImg = document.querySelector(".generated-img");
    let postUrl = encodeURI(document.location.href);
    let postTitle = encodeURI("Styled Image");
    let postImg = encodeURI(generatedImg.src);
 
    facebookBtn.setAttribute("href",`https://www.facebook.com/sharer.php?u=${postUrl}`);
    twitterBtn.setAttribute("href",`https://twitter.com/share?url=${postUrl}&text=${postTitle}`);
    whatsappBtn.setAttribute("href",`https://api.whatsapp.com/send?text=${postTitle} ${postUrl}`);
    linkedinBtn.setAttribute("href",`https://www.linkedin.com/shareArticle?url=${postUrl}&title=${postTitle}`);
    // facebookBtn.setAttribute("href",`https://www.facebook.com/sharer.php?u=${postUrl}`);
}
init();