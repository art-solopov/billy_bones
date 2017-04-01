const path = require('path');
const process = require('process');

const gulp = require('gulp');
const watch = require('gulp-watch');
const sass = require('gulp-sass');

const appPaths = process.env['APP_PATHS'].split(':');
const assetPaths = appPaths.map( p => path.join(p, 'assets'));

const stylesPaths = assetPaths.map( p => path.join(p, 'css') );
const scssPaths = stylesPaths.map( p => path.join(p, '[a-z]*.scss') );


gulp.task('css', () => {
    return gulp.src(scssPaths)
	       .pipe(sass({
		   includePaths:[
		       // TODO add libraries here
		       ...stylesPaths.map( p => path.join(p, 'shared'))
		   ]
	       }))
	       .pipe(gulp.dest(
		   f => {
		       let app = appPaths.find( x => f.path.startsWith(x) );
		       return path.normalize(path.join(app, 'static'));
		   }
	       ));
});

gulp.task('css:watch', () => {
    const paths = stylesPaths.map( p => path.join(p, '**', '*.scss') );
    console.log(paths);
    return watch(paths, () => { gulp.start('css'); });
});
