<!-- Example on how to make a Migration Update, adding a new Column to a table and adding
a foreing key as well -->
<!-- 
$ php artisan migrate
$ php artisan migrate:rollback

    
 -->
<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class AddStoreIdToUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('users', function (Blueprint $table) {

            // 1. Create new column
            // You probably want to make the new column nullable
            $table->integer('store_id')->unsigned()->nullable()->after('password');

            // 2. Create foreign key constraints
            $table->foreign('store_id')->references('id')->on('stores')->onDelete('SET NULL');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('users', function (Blueprint $table) {

            // 1. Drop foreign key constraints
            $table->dropForeign(['store_id']);

            // 2. Drop the column
            $table->dropColumn('store_id');
        });
    }
}