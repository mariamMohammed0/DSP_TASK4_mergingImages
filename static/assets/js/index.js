//Images
const image = document.getElementById('image');
const image2 = document.getElementById('image2');

//upload buttons
const custom_upload_btn = document.getElementById('custom_btn')
const custom_upload_btn2 = document.getElementById('custom_btn2');

//cropper.js
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
const cropper2 = new Cropper(image2, { zoomable: 0, aspectRatio: 0, viewMode: 0, });


//radio buttons of image 1 and their intial value
const mag1_radio = document.getElementById('img1_mag');
const phase1_radio = document.getElementById('img1_phase');
mag1_radio.checked = true;

//radio buttons of image 2 and their intial value
const mag2_radio = document.getElementById('img2_mag');
const phase2_radio = document.getElementById('img2_phase');
phase2_radio.checked = true;

//outside of the box checkbox
var outside_checkbox = 0;

//phase =1, Mag=0
var picture1_choice = 0;
var picture2_choice = 1;

//Intialization of output image
var flag =true;
if (flag== true)
{
    images_processing();
    flag=false;
}


//event listener for image 1
document.getElementById('pic1').addEventListener('click', function () {
    // console.log('ajax pic1')
    images_processing()
});

//event listener for image 2
document.getElementById('pic2').addEventListener('click', function () {
    // console.log('ajax pic2')
    images_processing();
});

//event listener for radiobuttons of image 1
document.getElementById('img1_radiobtn').addEventListener('click', function () {

    //get value of checked radiobutton
    radiobtn = document.querySelector('input[name="pic1_radio"]:checked').value;
    
    //change the value of the other radiobutton
    if (radiobtn!=picture1_choice)
        {
        if (radiobtn==0)
        {
            phase2_radio.checked = true;
            mag2_radio.checked = false;
            picture1_choice=0;
            picture2_choice=1;
        }
        else if (radiobtn==1)
        {
            phase2_radio.checked = false;
            mag2_radio.checked = true;
            picture1_choice=1;
            picture2_choice=0;
        }
        images_processing()           
    } 
});

//event listener for radiobuttons of image 2
document.getElementById('img2_radiobtn').addEventListener('click', function () {

    //get value of checked radiobutton
    radiobtn = document.querySelector('input[name="pic2_radio"]:checked').value;
    
    //change the value of the other radiobutton
    if (radiobtn!=picture2_choice)
    {
        if (radiobtn==0)
        {
            phase1_radio.checked = true;
            mag1_radio.checked = false;
            picture1_choice=1;
            picture2_choice=0;
        }
        else if (radiobtn==1)
        {
            phase1_radio.checked = false;
            mag1_radio.checked = true;
            picture1_choice=0;
            picture2_choice=1;
        }

        images_processing()
    }
});


function images_processing() 
{
    var data2 = cropper2.getCropBoxData();
    var data = cropper.getCropBoxData();


    //Intialize values for begining and uploading
    if (Object.keys(data).length==0)
    {
        data= { 'left': 50, 'top': 30, 'width': 400, 'height':240 };
    }

    if (Object.keys(data2).length==0)
    {
        data2= { 'left': 50, 'top': 30, 'width': 400, 'height':240 };
    }

    //sending data to back in the form of dictionary
    var pictures = { "pic1": data, "pic2": data2, "pic1_choice": picture1_choice, "pic2_choice": picture2_choice, "outside": outside_checkbox};

    $.ajax({
        url: "/crop_image1",
        type: "POST",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(pictures),
        success: function () {
            var d = new Date();
            var image1 = "../static/assets/images/outputs/output_image1.png?" + d.getMilliseconds();
            var image2 = "../static/assets/images/outputs/output_image2.png?" + d.getMilliseconds();

            $(".img1").attr("src", image1);
            $(".img2").attr("src", image2);
        }
    });
}



//upload button 1 functions
custom_upload_btn.addEventListener('click', function () {upload_btn.click();})
const upload_btn = document.getElementById('image_uploads');
upload_btn.addEventListener('change', updateImageDisplay);
function updateImageDisplay() {

    const curFiles = upload_btn.files;
    file_name = curFiles[0].name;
    var picture = { "pic": file_name, "index": 0 };
    $.ajax({
        url: "/save_image",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(picture),
    });
    flag=true;
    location.reload()
    
}

//upload button 2 functions
custom_upload_btn2.addEventListener('click', function () {upload_btn2.click();})
const upload_btn2 = document.getElementById('image_uploads2');
upload_btn2.addEventListener('change', updateImageDisplay2);
function updateImageDisplay2() {

    const curFiles2 = upload_btn2.files;
    file_name2 = curFiles2[0].name;
    var picture = { "pic": file_name2, "index": 1 };
    $.ajax({
        url: "/save_image",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(picture),
    });
    images_processing()
    location.reload()
    

}




//cropping outside the box functions
document.getElementById('outside').addEventListener('click', function () {

    radiobtn = document.querySelector('input[name="out_side"]:checked');
    if (radiobtn==null) 
    {
        outside_checkbox=0;

    }
    else
    {
        outside_checkbox = 1;
    }
    images_processing()
});
