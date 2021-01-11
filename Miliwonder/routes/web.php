<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});
Route::get('/index', function () {
    return view('products/index');
});
Route::get('/create', function () {
    return view('products/create');
});
Route::get('/show', function () {
    return view('products/show');
});
Route::get('/edit', function () {
    return view('products/edit');
});

Route::post('/index', function () {
    return view('products/index');
});
Route::post('/create', function () {
    return view('products/create');
});
Route::post('/show', function () {
    return view('products/show');
});
Route::post('/edit', function () {
    return view('products/edit');
});

Route::put('/index', function () {
    return view('products/index');
});
Route::put('/create', function () {
    return view('products/create');
});
Route::put('/show', function () {
    return view('products/show');
});
Route::put('/edit', function () {
    return view('products/edit');
});

Route::delete('/index', function () {
    return view('products/index');
});
Route::delete('/create', function () {
    return view('products/create');
});
Route::delete('/show', function () {
    return view('products/show');
});
Route::delete('/edit', function () {
    return view('products/edit');
});
Route::resource('products', ProductController::class);
