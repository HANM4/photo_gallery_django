let gulp = require('gulp');
let exec = require('child_process').exec;


gulp.task('tailwindcss', function (cb) {
  exec('npx tailwindcss -i ./photo_galirey/static/photo_galirey/css/input.css -o ./photo_galirey/static/photo_galirey/css/output.css', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
  });
});


gulp.task('watch', function(){
  gulp.watch('./templates/**/**.html', gulp.series(['tailwindcss']));
  gulp.watch('./photo_galirey/static/photo_galirey/css/input.css', gulp.series(['tailwindcss']));
});

exports.default = gulp.series(['tailwindcss', 'watch']);