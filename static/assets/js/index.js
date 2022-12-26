const image = document.getElementById('image');
const image2 = document.getElementById('image2');
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
const cropper2 = new Cropper(image2, { zoomable: 0, aspectRatio: 0, viewMode: 0, });

// document.getElementById('cropImageBtn').addEventListener('click', function () {

document.getElementById('pic1').addEventListener('click', function () {

    images_processing()
});


// document.getElementById('pic2').addEventListener('click', function () {
document.getElementById('pic2').addEventListener('click', function () {

    images_processing()
});

function images_processing() {
    // var croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
    // var croppedImage2 = cropper2.getCroppedCanvas().toDataURL('image/png');

    var data2 = cropper2.getCropBoxData();
    var data = cropper.getCropBoxData();

    var pic1_choice = document.querySelector('input[name="pic1_radio"]:checked');
    var pic2_choice = document.querySelector('input[name="pic2_radio"]:checked');

    if (pic1_choice != null) { pic1_choice = pic1_choice.value; }
    else { pic1_choice = 0 }

    if (pic2_choice != null) { pic2_choice = pic2_choice.value; }
    else { pic1_choice = 1 }


    var pictures = { "pic1": data, "pic2": data2, "pic1_choice": pic1_choice, "pic2_choice": pic2_choice };


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

    // var d = new Date(); 
    // var image="../static/assets/images/outputs/output_image1.png?"+d.getMilliseconds(); //pic.src(image);
    // document.getElementById('output1').src = image;
    // document.getElementById('output2').src = "../static/assets/images/outputs/output_image2.png?random";

    // $(".img2").attr("src",image);
}
const upload_btn = document.getElementById('image_uploads');
upload_btn.addEventListener('change', updateImageDisplay);
function updateImageDisplay() {

    const curFiles = upload_btn.files;
    file_name = curFiles[0].name;
    console.log(curFiles[0].name)
    // sr="--------------------------------------"
    // console.log(sr)

    $.ajax({
        url: "/save_image",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(file_name),
    });
    // console.log("--------------------------------------")

}