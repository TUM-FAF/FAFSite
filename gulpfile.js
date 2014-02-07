var gulp = require('gulp')
  // utils
  , gutil = require('gulp-util')
  , clean = require('gulp-clean')
  , path = require('path')
  , watch = require('gulp-watch')
  // styles
  , stylus = require('gulp-stylus')
  , less = require('gulp-less')
  , csso = require('gulp-csso')
  // js
  , coffee = require('gulp-coffee')
  , uglify = require('gulp-uglify')
  // server
  , lr = require('tiny-lr')
  , livereload = require('gulp-livereload')
  , server = lr()
  ;

// Build
gulp.task('b', ['build'])
gulp.task('build', ['build-bootstrap'], function(){
  // Stylesheet
  gulp.src('./src/style/style.styl')
    .pipe(stylus({use: ['nib'], set: ['include css']}))
    .pipe(csso(false))
    .pipe(gulp.dest('./fafsite/static/css'))

  // Scripts
  gulp.src('./src/script/*.coffee')
    .pipe(coffee({bare: true, join: true}).on('error', gutil.log))
    .pipe(uglify())
    .pipe(gulp.dest('./fafsite/static/js'))

  // Clean maps
  gulp.src('./fafsite/static/**/*.map')
    .pipe(clean())
})
gulp.task('build-bootstrap', function(){
  gulp.src('./src/style/bootstrap/bootstrap.less')
    .pipe(less())
    .pipe(gulp.dest('./src/components/bootstrap/dist/css'))
})

// Development
gulp.task('d', ['development'])
gulp.task('default', ['development']);
gulp.task('development', ['development-style', 'development-script'], function(){})
gulp.task('development-style', ['development-stylus-full'])
gulp.task('development-stylus-full', ['development-bootstrap'], function(){
  // Stylesheet
  return gulp.src('./src/style/style.styl')
    .pipe(stylus({use: ['nib'], set: ['include css', 'linenos']}).on('error', gutil.log))
    .pipe(gulp.dest('./fafsite/static/css'))
    .pipe(livereload(server))
})
gulp.task('development-stylus', function(){
  // Stylesheet
  return gulp.src('./src/style/style.styl')
    .pipe(stylus({use: ['nib'], set: ['include css', 'linenos']}).on('error', gutil.log))
    .pipe(gulp.dest('./fafsite/static/css'))
    .pipe(livereload(server))
})
gulp.task('development-bootstrap', function(){
  // Stylesheet
  return gulp.src('./src/style/bootstrap/bootstrap.less')
    .pipe(less().on('error', gutil.log))
    .pipe(gulp.dest('./src/components/bootstrap/dist/css'))
})
gulp.task('development-script', function(){
  // Scripts
  return gulp.src('./src/script/*.coffee')
    .pipe(coffee({bare: true, join: true, sourceMap: true}).on('error', gutil.log))
    .pipe(gulp.dest('./fafsite/static/js'))
    .pipe(livereload(server))
})

// Watch
gulp.task('w', ['_watch'])
gulp.task('_watch', ['development', 'listen'], function(){
  // Watch stylus style changes
  var watcher_style = gulp.watch('./src/style/**/*.styl', ['development-stylus'])
  watcher_style.on('changed', function(e){
    console.log(e.type + '-' + e.path)
  })

  // Watch bootstrap source changes
  var watcher_bootstrap = gulp.watch('./src/style/bootstrap/**/*', ['development-style'])
  watcher_bootstrap.on('changed', function(e){
    console.log(e.type + '-' + e.path)
  })

  // Watch script changes
  var watcher_script = gulp.watch('./src/script/**/*', ['development-script'])
  watcher_script.on('changed', function(e){
    console.log(e.type + '-' + e.path)
  })

  // Watch template changes
  gulp.src('./fafsite/templates/**/*', {read: false})
    .pipe(watch())
    .pipe(livereload(server))
})

// Listen
gulp.task('listen', function(next) {
  server.listen(35729, function(err) {
    if (err) return console.error(err)
    next()
  })
})

// Test
gulp.task('t', ['test'])
gulp.task('test', function(){
  //
})
