document.getElementById('demo').innerHTML = "This was created with javascript";
$(document).ready(function(){
  $("#hide").click(function(){
    $("#ape").hide();
  });
  $("#show").click(function(){
    $("#ape").show();
  });
});


$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").slideDown("slow");
  });
});






navigator.mediaDevices.getUserMedia({ audio: true }).then(
  (stream) => {
    const recorder = new MediaRecorder(stream)

    recorder.onstart = async () => {
      await fetch("/stream/upload", {
        method: "POST",
        headers: { "Content-Type": "multipart/form-data" },
        body: stream,
        allowHTTP1ForStreamingUpload: true,
      })

      console.log("Upload complete!")
    }
  },
  (err) => console.error("Error: " + err)
)
