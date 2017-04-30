const path = require('path');

const webpack = require('webpack');

const ExtractTextPlugin = require('extract-text-webpack-plugin');
const env = require('process').env;

const dist = path.resolve(__dirname, 'home/static/');

module.exports = {
    entry: ['./assets/js/index.js', './assets/css/index.css'],
    output: {
	filename: 'application.js',
	path: dist
    },
    module: {
	rules: [
	    {
		test: /\.(css|scss)$/,
		use: ExtractTextPlugin.extract({
		    fallback: 'style-loader',
		    use: ['css-loader', 'sass-loader']
		})
	    },
	    {
		test: /\.js$/,
		exclude: /(node_modules|bower_components)/,
		use: {
		    loader: 'babel-loader',
		    options: {
			presets: ['env']
		    }
		}
	    },
	    {
		test: /\.(jpeg|png|gif|svg|eot|ttf|woff|woff2)$/i,
		use: [{
		    loader: 'file-loader',
		    options: {
			dist,
			name: env.NODE_ENV === 'production' ? '[name]-[hash].[ext]' : '[name].[ext]',
			publicPath: env.NODE_ENV === 'production' ? '/static/' : 'http://localhost:12800/'
		    }
		}]

	    }
	]
    },
    plugins: [
	new ExtractTextPlugin('application.css'),
	new webpack.ProvidePlugin({
	    $: 'jquery',
	    jQuery: 'jquery'
	})
    ],
    devServer: {
	contentBase: dist,
	compress: true,
	port: 12800
    }
};
