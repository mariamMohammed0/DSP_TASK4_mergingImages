const image = document.getElementById('image');
const cropper = new Cropper(image, { zoomable: 0, aspectRatio: 0, viewMode: 0, });
document.getElementById('cropImageBtn').addEventListener('click', function () {
    var croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
    var data = cropper.getCropBoxData();

    console.log(data)
    document.getElementById('output').src = croppedImage;
});
