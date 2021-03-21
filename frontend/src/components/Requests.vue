<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Requests</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.request-modal
        @click="onAddRequest">
          Add Request
        </button>
        <br>
        <br>
        <input type="text" v-model="search" placeholder="search requests" />
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Request Name</th>
              <th scope="col">Description</th>
              <th scope="col">Status</th>
              <th scope="col">Created By</th>
              <th scope="col">Updated?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(request, index) in filteredRequests" :key="index">
              <!-- <td>{{ request.requestid }}</td> -->
              <td>{{ request.name }}</td>
              <td>{{ request.description }}</td>
              <td>{{ request.status }}</td>
              <td>{{ request.createdby }}</td>
              <td>
                <span v-if="request.updated">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.request-update-modal
                          @click="editRequest(request)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteRequest(request)">
                      Delete
                  </button>
                  <button
                          type="button"
                          class="btn btn-primary btn-sm"
                          v-b-modal.request-upload-modal
                          @click="uploadRequest(request)">
                      Uplaod
                  </button>
                  <button
                          type="button"
                          class="btn btn-info btn-sm"
                          @click="downloadRequest(request)">
                      Download
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <AddRequest v-show="this.showAddForm" @add-request="addRequest" />
    <EditRequest v-show="this.showEditForm" @update-request="updateRequest" v-bind="this.request" />
    <b-modal ref="uploadRequestModal"
            id="request-upload-modal"
            title="Upload"
            hide-footer>
        <b-form @submit.prevent="onSubmitUpload" class="w-100">
          <b-form-file v-model="uploadedFile" class="mt-3" plain></b-form-file>
          <div class="mt-3">Selected file: {{ uploadedFile ? uploadedFile.name : '' }}</div>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import AddRequest from './AddRequest.vue';
import EditRequest from './EditRequest.vue';

export default {
  name: "Requests",
  // props: {
  //       showForm: Boolean,
  // },
  components: {
    // AddRequest: () => import('./AddRequest.vue')
    AddRequest,
    EditRequest,
  },
  data() {
    return {
      showAddForm: false,
      showEditForm: false,
      requests: [],
      search:'',     
      message: '',
      showMessage: false,
      request: {
        requestid: '',
        name: '',
        description: '',
        status: '',
        createdby: '',
        updated: []
      },
      file: '',
      uploadedFile: null
    };
  },
  computed: {
    filteredRequests: function() {
      return this.requests.filter(request => {
        return request.name.match(this.search)
      })
    }

  },
  components: {
    alert: Alert,
  },
  methods: {
    getRequests() {
      const path = 'http://localhost:5000/requests/all';
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.get(path, optionAxios)
        .then((res) => {
          this.requests = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onAddRequest(){
      this.showAddForm = true;
    },
    addRequest(payload) {
      const path = 'http://localhost:5000/requests/add';
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.post(path, payload, optionAxios)
        .then(() => {
          console.log(`Print payload: ${payload}`)
          this.getRequests();
          this.message = 'Request added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(`Post Req Error: ${error}`);
          this.getRequests();
        });
    },    
    uploadRequest(request) {
      this.editForm = request;
    },
    onSubmitUpload() {
      this.$refs.uploadRequestModal.hide();
      console.log(this.uploadedFile)
      let requestID = this.editForm.requestid;
      let formData = new FormData();
      formData.append('image', this.uploadedFile);
       for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
    }
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token'),
               'Content-Type': 'multipart/form-data'
            }
        }
      const path = `http://localhost:5000/requests/upload/${requestID}`;
      axios.post(path, formData, optionAxios)
          .then(() => {
            this.getRequests();
            this.message = 'File uploaded!';
            this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          // this.getRequests();
        });
    },
    downloadRequest(request) {
      // this.$refs.uploadRequestModal.hide();
      let requestID = request.requestid;

      const path = `http://localhost:5000/requests/download/${requestID}`;
      axios({
        url: path,
        method: 'GET',
        responseType: 'blob',
        headers: {Authorization: "Bearer " + localStorage.getItem('vue-token')}
      }).then(response => {

        var fileURL=window.URL.createObjectURL(new Blob([response.data]));
        var fileLink=document.createElement('a');
        fileLink.href=fileURL;
        fileLink.setAttribute('download', 'report.pdf');
        document.body.appendChild(fileLink);
        fileLink.click();
      }).catch(error => {
        console.log(error);
      });
    },
    editRequest(request) {
      this.showEditForm = true;
      this.request = request;
    },   
    updateRequest(payload, requestID) {
      const path = `http://localhost:5000/requests/${requestID}`;
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.put(path, payload, optionAxios)
        .then(() => {
          this.getRequests();
          this.message = 'Request updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editRequestModel.hide();
      this.initForm();
      this.getRequests(); // why?
    },
    removeRequest(requestID) {
      const path = `http://localhost:5000/requests/${requestID}`;
      var optionAxios = {
            headers: {
               Authorization: "Bearer " + localStorage.getItem('vue-token')
            }
        }
      axios.delete(path, optionAxios)
        .then(() => {
          this.getRequests();
          this.message = 'Request removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getRequests();
        });
    },
    onDeleteRequest(request) {
      console.log(request)
      this.removeRequest(request.requestid);
    },
  },
  created() {
    this.getRequests();
  },
};
</script>
