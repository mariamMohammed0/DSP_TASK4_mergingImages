const image = document.getElementById('image');
const image2 = document.getElementById('image2');
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
const cropper2 = new Cropper(image2, { zoomable: 0, aspectRatio: 0, viewMode: 0, });

// document.getElementById('cropImageBtn').addEventListener('click', function () {
    document.getElementById('pic1').addEventListener('click', function () {
        var croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
        var croppedImage2 = cropper2.getCroppedCanvas().toDataURL('image/png');
        var data2 = cropper2.getCropBoxData();
        var data = cropper.getCropBoxData();
        // var pictures={"pic1":data,"pic2":data2}
        var pic1_choice= document.querySelector( 'input[name="pic1_radio"]:checked'); 
        if(pic1_choice != null) {pic1_choice= pic1_choice.value; }
        var pic2_choice= document.querySelector( 'input[name="pic2_radio"]:checked'); 
        if(pic2_choice != null) {pic2_choice= pic2_choice.value; }
        var pictures={"pic1":data,"pic2":data2,"pic1_choice":pic1_choice,"pic2_choice":pic2_choice};
        // document.getElementById('output').src = croppedImage;
        $.ajax({
            url:"/crop_image1",
            type:"POST",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(pictures)});
    });
    // document.getElementById('pic2').addEventListener('click', function () {
    document.getElementById('pic2').addEventListener('click', function () {
        var croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
        var croppedImage2 = cropper2.getCroppedCanvas().toDataURL('image/png');
        var data2 = cropper2.getCropBoxData();
        var data = cropper.getCropBoxData();
        
        var pic1_choice= document.querySelector( 'input[name="pic1_radio"]:checked'); 
        if(pic1_choice != null) {pic1_choice= pic1_choice.value; }
        var pic2_choice= document.querySelector( 'input[name="pic2_radio"]:checked'); 
        if(pic2_choice != null) {pic2_choice= pic2_choice.value; }
        var pictures={"pic1":data,"pic2":data2,"pic1_choice":pic1_choice,"pic2_choice":pic2_choice};
        // document.getElementById('output').src = croppedImage;
        
        $.ajax({
            url:"/crop_image1",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(pictures)});
    });