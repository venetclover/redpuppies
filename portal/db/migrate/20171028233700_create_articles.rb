class CreateArticles < ActiveRecord::Migration[5.1]
  def change
    create_table :houses do |t|
      t.string  :title
      t.string  :mls
      t.integer :price
      t.integer :size
      t.integer :bed
      t.integer :bath
      t.integer :hoa
      t.string  :url
      t.string  :house_type
      t.string  :address
      t.string  :city
      t.string  :state
      t.integer :zip
      t.string  :status
      t.integer :year_built
      t.string  :geo_point

      t.timestamps
    end
  end
end
