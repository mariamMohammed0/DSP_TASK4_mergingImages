const image = document.getElementById('image');
const image2 = document.getElementById('image2');
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
const cropper2 = new Cropper(image2, { zoomable: 0, aspectRatio: 0, viewMode: 0, });

document.getElementById('cropImageBtn').addEventListener('click', function () {
    var croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
    var data = cropper.getCropBoxData();
    document.getElementById('output').src = croppedImage;
    $.ajax({
        url:"/crop_image1",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(data)});
});
document.getElementById('cropImageBtn2').addEventListener('click', function () {
    var croppedImage2 = cropper2.getCroppedCanvas().toDataURL('image/png');
    var data2 = cropper2.getCropBoxData();
    document.getElementById('output').src = croppedImage2;
    
    $.ajax({
        url:"/crop_image2",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(data2)});
});
