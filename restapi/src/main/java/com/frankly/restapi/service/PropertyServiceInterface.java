package com.frankly.restapi.service;

import com.frankly.restapi.domain.PropertyChangeDTO;
import com.frankly.restapi.domain.PropertyDTO;

import java.util.List;

public interface PropertyServiceInterface {

    public void createProperty(PropertyDTO propertyDTO) throws Exception;

    public List<PropertyDTO>readProperty(int politicianID) throws Exception;

    public List<PropertyChangeDTO>readPropertyChange(int politicianID) throws Exception;

    public void updateProperty(PropertyDTO propertyDTO) throws Exception;

    public void deleteProperty(PropertyDTO propertyDTO)throws Exception;

}
