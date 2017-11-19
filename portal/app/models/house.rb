class House < ActiveRecord::Base
  searchkick word_start: [:title, :house_type]
end
