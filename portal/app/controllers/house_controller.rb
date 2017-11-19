class HouseController < ApplicationController

  def index
    @house = House.search("*", load: false)
    return nil unless @house.size

    @house
  end

  def autocomplete
    render json: House.search(params[:query], {
      fields: ["title^5", "house_type"],
      match: :word_start,
      limit: 10,
      load: false,
      misspellings: {below: 5}
    }).map(&:title)
  end
end
