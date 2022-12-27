const image = document.getElementById('image');
const image2 = document.getElementById('image2');
const custom_btn = document.getElementById('custom_btn')
const custom_btn2 = document.getElementById('custom_btn2');
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
const cropper2 = new Cropper(image2, { zoomable: 0, aspectRatio: 0, viewMode: 0, });

const mag1_radio = document.getElementById('img1_mag');
const phase1_radio = document.getElementById('img1_phase');
mag1_radio.checked = true;

const mag2_radio = document.getElementById('img2_mag');
const phase2_radio = document.getElementById('img2_phase');
phase2_radio.checked = true;


document.getElementById('pic1').addEventListener('click', function () {
    images_processing()
});


document.getElementById('pic2').addEventListener('click', function () {

    images_processing();
});

document.getElementById('img1_radiobtn').addEventListener('click', function () {

    radiobtn = document.querySelector('input[name="pic1_radio"]:checked').value;
    // console.log(radiobtn)
    if (radiobtn==0)
    {
        phase2_radio.checked = true;
        mag2_radio.checked = false;
    }
    else if (radiobtn==1)
    {
        phase2_radio.checked = false;
        mag2_radio.checked = true;
    }

    
    images_processing()           
    
});

document.getElementById('img2_radiobtn').addEventListener('click', function () {

    radiobtn = document.querySelector('input[name="pic2_radio"]:checked').value;
    console.log(radiobtn)
    if (radiobtn==0)
    {
        phase1_radio.checked = true;
        mag1_radio.checked = false;
    }
    else if (radiobtn==1)
    {
        phase1_radio.checked = false;
        mag1_radio.checked = true;
    }


    images_processing()
});


function images_processing() 
{

    var data2 = cropper2.getCropBoxData();
    var data = cropper.getCropBoxData();

    var c1 =  document.querySelector('input[name="pic1_radio"]:checked').value;
    var c2 = document.querySelector('input[name="pic2_radio"]:checked').value;


    var pictures = { "pic1": data, "pic2": data2, "pic1_choice": c1, "pic2_choice": c2 };


    $.ajax({
        url: "/crop_image1",
        type: "POST",
        contentType: "application/json",
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








const upload_btn = document.getElementById('image_uploads');
upload_btn.addEventListener('change', updateImageDisplay);
function updateImageDisplay() {

    const curFiles = upload_btn.files;
    file_name = curFiles[0].name;
    console.log(curFiles[0].name)
    var picture = { "pic": file_name, "index": 0 };
    $.ajax({
        url: "/save_image",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(picture),
    });

}
const upload_btn2 = document.getElementById('image_uploads2');
upload_btn2.addEventListener('change', updateImageDisplay2);
function updateImageDisplay2() {

    const curFiles2 = upload_btn2.files;
    file_name2 = curFiles2[0].name;
    console.log(curFiles2[0].name)
    var picture = { "pic": file_name2, "index": 1 };
    $.ajax({
        url: "/save_image",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(picture),
    });


}
custom_btn.addEventListener('click', function () {
    upload_btn.click();
})
custom_btn2.addEventListener('click', function () {
    upload_btn2.click();
})